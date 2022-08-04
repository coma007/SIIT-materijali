package examples;

import java.io.IOException;
import org.apache.lucene.document.Document;
import org.apache.lucene.search.ScoreDoc;
import org.apache.lucene.search.TopDocs;
import org.apache.lucene.search.Query;
import org.apache.lucene.analysis.Analyzer;
import org.apache.lucene.index.IndexReader;
import org.apache.lucene.index.LeafReaderContext;

import java.util.Date;
import java.util.HashSet;

import org.apache.lucene.queryparser.classic.QueryParser;
import java.io.Reader;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.nio.file.Files;
import java.nio.charset.StandardCharsets;
import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.search.IndexSearcher;
import org.apache.lucene.store.Directory;
import org.apache.lucene.index.DirectoryReader;
import org.apache.lucene.store.FSDirectory;
import java.nio.file.Paths;

public class SearchFiles
{
    private SearchFiles() {
    }
    
    //TODO prosiriti/promeniti kod tako da ne pretrazuje na osnovu sadrzaja datoteke, vec na osovu naziva
    //TODO testirati upite sa OR AND i NOT klauzulama, i upit sa regularnim izrazima
    public static void main(final String[] args) throws Exception {
        System.out.println("Working Directory = " + System.getProperty("user.dir"));
        final String usage = "Usage:\tjava org.apache.lucene.demo.SearchFiles [-index dir] [-field f] [-repeat n] [-queries file] [-query string] [-raw] [-paging hitsPerPage]\n\nSee http://lucene.apache.org/core/4_1_0/demo/ for details.";
        if (args.length > 0 && ("-h".equals(args[0]) || "-help".equals(args[0]))) {
            System.out.println(usage);
            System.exit(0);
        }
        //Ako korisnik nije uneo putanju gde se nalazi izgradjen index kroz parametar, pretpostavljamo da se putanja nalazi
        String index = ".";
        String field = "contents";
        String queries = null;
        int repeat = 0;
        boolean raw = false;
        String queryString = null;
        int hitsPerPage = 10;
        //Parsiranje argumenata sa komandne linije (u 31. liniji mozete videti koji argumenti se ocekuju)
        for (int i = 0; i < args.length; ++i) {
            if ("-index".equals(args[i])) {
                index = args[i + 1];
                ++i;
            }
            else if ("-field".equals(args[i])) {
                field = args[i + 1];
                ++i;
            }
            else if ("-queries".equals(args[i])) {
                queries = args[i + 1];
                ++i;
            }
            else if ("-query".equals(args[i])) {
                queryString = args[i + 1];
                ++i;
            }
            else if ("-repeat".equals(args[i])) {
                repeat = Integer.parseInt(args[i + 1]);
                ++i;
            }
            else if ("-raw".equals(args[i])) {
                raw = true;
            }
            else if ("-paging".equals(args[i])) {
                hitsPerPage = Integer.parseInt(args[i + 1]);
                if (hitsPerPage <= 0) {
                    System.err.println("There must be at least 1 hit per page.");
                    System.exit(1);
                }
                ++i;
            }
        }
        //Default-an poziv objekata/metoda koji treba da ucitaju prethodno kreiran indeks i vrse pretrage nad njim
        final IndexReader reader = (IndexReader)DirectoryReader.open((Directory)FSDirectory.open(Paths.get(index, new String[0])));
        final IndexSearcher searcher = new IndexSearcher(reader);
        final Analyzer analyzer = (Analyzer)new StandardAnalyzer();
                
        BufferedReader in = null;
        if (queries != null) {
            in = Files.newBufferedReader(Paths.get(queries, new String[0]), StandardCharsets.UTF_8);
        }
        else {
            in = new BufferedReader(new InputStreamReader(System.in, StandardCharsets.UTF_8));
        }
        final QueryParser parser = new QueryParser(field, analyzer);
        do {
            if (queries == null && queryString == null) {
                System.out.println("Enter query: ");
            }
            String line = (queryString != null) ? queryString : in.readLine();
            if (line == null) {
                break;
            }
            if (line.length() == -1) {
                break;
            }
            line = line.trim();
            if (line.length() == 0) {
                break;
            }
            final Query query = parser.parse(line);
            System.out.println("Searching for: " + query.toString(field));
            if (repeat > 0) {
                final Date start = new Date();
                for (int j = 0; j < repeat; ++j) {
                    searcher.search(query, 100);
                }
                final Date end = new Date();
                System.out.println("Time: " + (end.getTime() - start.getTime()) + "ms");
            }
            doPagingSearch(in, searcher, query, hitsPerPage, raw, queries == null && queryString == null);
        } while (queryString == null);
        reader.close();
    }
    
    
    public static void doPagingSearch(final BufferedReader in, final IndexSearcher searcher, final Query query, final int hitsPerPage, final boolean raw, final boolean interactive) throws IOException {
        //Ovo je sustina, jedna od glavnih metoda oko koje je citav ovaj primer napisan - metoda koja zapravo uzima objekat upita(Query), i izvrsava ga nad ucitanim indeksom
    	//Upaliti debugger i pogledati sta sadrze objekti Query, TopDocs i ScoreDoc klasa
    	final TopDocs results = searcher.search(query, 5 * hitsPerPage);
        ScoreDoc[] hits = results.scoreDocs;
        
        
        final int numTotalHits = Math.toIntExact(results.totalHits.value);
        System.out.println(numTotalHits + " total matching documents");
        int start = 0;
        int end = Math.min(numTotalHits, hitsPerPage);
        while (true) {
            if (end > hits.length) {
                System.out.println("Only results 1 - " + hits.length + " of " + numTotalHits + " total matching documents collected.");
                System.out.println("Collect more (y/n) ?");
                final String line = in.readLine();
                if (line.length() == 0) {
                    break;
                }
                if (line.charAt(0) == 'n') {
                    break;
                }
                hits = searcher.search(query, numTotalHits).scoreDocs;
            }
            end = Math.min(hits.length, start + hitsPerPage);
            for (int i = start; i < end; ++i) {
                if (raw) {
                    System.out.println("doc=" + hits[i].doc + " score=" + hits[i].score);
                }
                else {
                	//Prosiriti ispis da ispisu i "score" koji je svaki dokument dobio za dati upit
                    final Document doc = searcher.doc(hits[i].doc);
                    final String path = doc.get("path");
                    if (path != null) {
                        System.out.println(i + 1 + ". " + path);
                        final String title = doc.get("title");
                        if (title != null) {
                            System.out.println("   Title: " + doc.get("title"));
                        }
                    }
                    else {
                        System.out.println(i + 1 + ". No path for this document");
                    }
                }
            }
            if (!interactive) {
                break;
            }
            if (end == 0) {
                break;
            }
            if (numTotalHits < end) {
                continue;
            }
            boolean quit = false;
            while (true) {
                System.out.print("Press ");
                if (start - hitsPerPage >= 0) {
                    System.out.print("(p)revious page, ");
                }
                if (start + hitsPerPage < numTotalHits) {
                    System.out.print("(n)ext page, ");
                }
                System.out.println("(q)uit or enter number to jump to a page.");
                final String line2 = in.readLine();
                if (line2.length() == 0 || line2.charAt(0) == 'q') {
                    quit = true;
                    break;
                }
                if (line2.charAt(0) == 'p') {
                    start = Math.max(0, start - hitsPerPage);
                    break;
                }
                if (line2.charAt(0) == 'n') {
                    if (start + hitsPerPage < numTotalHits) {
                        start += hitsPerPage;
                        break;
                    }
                    break;
                }
                else {
                    final int page = Integer.parseInt(line2);
                    if ((page - 1) * hitsPerPage < numTotalHits) {
                        start = (page - 1) * hitsPerPage;
                        break;
                    }
                    System.out.println("No such page");
                }
            }
            if (quit) {
                break;
            }
            end = Math.min(numTotalHits, start + hitsPerPage);
        }
    }
}
