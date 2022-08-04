package examples;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.Reader;
import java.io.StringReader;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.LinkOption;
import java.nio.file.OpenOption;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Date;
import java.util.List;
import java.util.stream.Collectors;

import org.apache.lucene.analysis.Analyzer;
import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.document.Document;
import org.apache.lucene.document.Field;
import org.apache.lucene.document.LongPoint;
import org.apache.lucene.document.StringField;
import org.apache.lucene.document.TextField;
import org.apache.lucene.index.IndexWriter;
import org.apache.lucene.index.IndexWriterConfig;
import org.apache.lucene.index.IndexableField;
import org.apache.lucene.index.Term;
import org.apache.lucene.store.Directory;
import org.apache.lucene.store.FSDirectory;

public class IndexFiles
{
    private IndexFiles() {
    }
    
    //TODO: DONE promeniti destinaciju (putanju na kojoj se cuva index) index-a
    public static void main(final String[] args) {
        final String usage = "java org.apache.lucene.demo.IndexFiles [-index INDEX_PATH] [-docs DOCS_PATH] [-update]\n\nThis indexes the documents in DOCS_PATH, creating a Lucene indexin INDEX_PATH that can be searched with SearchFiles";
        String indexPath = ".";
        String docsPath = null;
        boolean create = true;
        for (int i = 0; i < args.length; ++i) {
            if ("-index".equals(args[i])) {
                indexPath = args[i + 1];
                ++i;
            }
            else if ("-docs".equals(args[i])) {
                docsPath = args[i + 1];
                ++i;
            }
            else if ("-update".equals(args[i])) {
                create = false;
            }
        }
        if (docsPath == null) {
            System.err.println("Usage: " + usage);
            System.exit(1);
        }
        final Path docDir = Paths.get(docsPath, new String[0]);
        if (!Files.isReadable(docDir)) {
            System.out.println("Document directory '" + docDir.toAbsolutePath() + "' does not exist or is not readable, please check the path");
            System.exit(1);
        }
        final Date start = new Date();
        try {
            System.out.println("Indexing to directory '" + indexPath + "'...");
            final Directory dir = (Directory)FSDirectory.open(Paths.get(indexPath, new String[0]));
            //Komponenta koja prolazi kroz sve dokumente i niz karaktera (reci) pretvara u niz tokena na osnovu kojih se gradi index (index-i)
            final Analyzer analyzer = (Analyzer)new StandardAnalyzer();
            final IndexWriterConfig iwc = new IndexWriterConfig(analyzer);
            if (create) {
                iwc.setOpenMode(IndexWriterConfig.OpenMode.CREATE);
            }
            else {
                iwc.setOpenMode(IndexWriterConfig.OpenMode.CREATE_OR_APPEND);
            }
            final IndexWriter writer = new IndexWriter(dir, iwc);
            indexDocs(writer, docDir);
            writer.close();
            final Date end = new Date();
            System.out.println(end.getTime() - start.getTime() + " total milliseconds");
        }
        catch (IOException e) {
            System.out.println(" caught a " + e.getClass() + "\n with message: " + e.getMessage());
        }
    }
    
    // TODO: DONE prosiriti da ovo radi rekurzivno, i da indeksira i fajlove u sub-folderima
    static void indexDocs(final IndexWriter writer, final Path path) throws IOException {
    	if (Files.isDirectory(path, new LinkOption[0])) {
            List<Path> all_paths = Files.list(path).collect(Collectors.toList());
            for(Path current_path:all_paths) {
            	System.out.println(current_path.toString());
            	if(!Files.isDirectory(current_path, new LinkOption[0])) {
            		indexDoc(writer, current_path, Files.getLastModifiedTime(path, new LinkOption[0]).toMillis());
            	}
            	else {
            		indexDocs(writer, current_path);
            	}
            }
        }
        else {
            indexDoc(writer, path, Files.getLastModifiedTime(path, new LinkOption[0]).toMillis());
        }
    }
    
    static void indexDoc(final IndexWriter writer, final Path file, final long lastModified) throws IOException {
        try (final InputStream stream = Files.newInputStream(file, new OpenOption[0])) {
            final Document doc = new Document();
            final Field pathField = (Field)new StringField("path", file.toString(), Field.Store.YES);
            doc.add((IndexableField)pathField);
            doc.add((IndexableField)new LongPoint("modified", new long[] { lastModified }));
            doc.add((IndexableField)new TextField("contents", (Reader)new BufferedReader(new InputStreamReader(stream, StandardCharsets.UTF_8))));
            //TODO DONE prosiriti da indeks nije samo za polje "contents" (sadrzaj dokumenta) vec da ima i za naziv fajla-a
            doc.add((IndexableField)new TextField("filename", new StringReader(file.getFileName().toString())));
            BufferedReader reader = new BufferedReader(new FileReader(file.toString()));
            String line;
            String allContents = "";
            while ((line = reader.readLine()) != null) {
            	if (line.equals("")) {
            		line = "\n";
            	}
            	allContents += line;
            }
            String[] data = allContents.split("\n");
            String header = data[0];
            String conclusion = "";
            try {
            	conclusion = data[data.length - 1];
            }
            catch (Exception e) {
            }
            doc.add((IndexableField)new TextField("header", new StringReader(header)));
            doc.add((IndexableField)new TextField("conclusion", new StringReader(conclusion)));
            
            BufferedReader lines = new BufferedReader(new FileReader(file.toString()));
            String firstLine = lines.readLine();
            
            doc.add((IndexableField)new TextField("firstline", new StringReader(firstLine)));
            doc.add((IndexableField)new TextField("otherlines", lines));
            
            if (writer.getConfig().getOpenMode() == IndexWriterConfig.OpenMode.CREATE) {
                System.out.println("adding " + file);
                writer.addDocument((Iterable)doc);
            }
            else {
                System.out.println("updating " + file);
                writer.updateDocument(new Term("path", file.toString()), (Iterable)doc);
            }
        }
    }
}