package examples;

import java.io.InputStream;
import org.apache.lucene.index.Term;
import org.apache.lucene.document.TextField;
import java.io.Reader;
import java.io.StringReader;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import org.apache.lucene.document.LongPoint;
import org.apache.lucene.index.IndexableField;
import org.apache.lucene.document.StringField;
import org.apache.lucene.document.Field;
import org.apache.lucene.document.Document;
import java.nio.file.OpenOption;
import java.nio.file.FileVisitResult;
import java.nio.file.FileVisitor;
import java.nio.file.LinkOption;
import org.apache.lucene.analysis.Analyzer;
import org.apache.lucene.store.Directory;
import java.nio.file.Path;
import java.io.IOException;
import org.apache.lucene.index.IndexWriter;
import org.apache.lucene.index.IndexWriterConfig;
import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.store.FSDirectory;
import java.util.Date;
import java.util.List;
import java.util.stream.Collectors;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.file.SimpleFileVisitor;
import java.nio.file.attribute.BasicFileAttributes;

public class IndexFiles
{
    private IndexFiles() {
    }
    
    //TODO promeniti destinaciju (putanju na kojoj se cuva index) index-a
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
    
    //TODO: prosiriti da ovo radi rekurzivno, i da indeksira i fajlove u sub-folderima
    static void indexDocs(final IndexWriter writer, final Path path) throws IOException {
    	if (Files.isDirectory(path, new LinkOption[0])) {
            List<Path> all_paths = Files.list(path).collect(Collectors.toList());
            for(Path current_path:all_paths) {
            	System.out.println(current_path.toString());
            	if(!Files.isDirectory(current_path, new LinkOption[0])) {
            		indexDoc(writer, current_path, Files.getLastModifiedTime(path, new LinkOption[0]).toMillis());
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
            doc.add((IndexableField)new TextField("title", new StringReader(file.getFileName().toString())));
            //TODO prosiriti da indeks nije samo za polje "contents" (sadrzaj dokumenta) vec da ima i za naziv fajla-a
            //doc.add((IndexableField)new TextField("title", new StringReader(file.getFileName().toString())));
            BufferedReader reader = new BufferedReader(new FileReader(file.toFile()));
            String firstLine = reader.readLine();
            doc.add((IndexableField)new TextField("articleTitle", new StringReader(firstLine)));
            doc.add((IndexableField)new TextField("articleContents", reader));
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