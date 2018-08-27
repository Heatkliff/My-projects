package projects.ParcerIT;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import java.io.*;
import java.util.ArrayList;
import java.util.HashMap;


public class Main2 {

    private static Document document, underDocument;
    private static Elements elements, underElements;
    private static String idImage = "";
    private static PrintWriter writer;
    private static ArrayList<String> nameSite;
    private static ArrayList<String> nameSurf;
    private static String site = "https://vchasah-test.com.46-4-107-52.brv.com.ua/index.php?route=product/search&search=";

    public static void main(String[] args) throws Exception {
       readList();
        /**
         * поиск нужных елементов
         */
        for (String element : nameSurf) {
            document = Jsoup.connect(site+element).get();
            elements = document.select("div.goods-catalog");
            System.out.println(elements);
        }
    }

    private static void readList(){
        /**
         * Счивание нужных элементов с файла
         */
        try {
            nameSurf = new ArrayList<String>();
            BufferedReader br = new BufferedReader(new FileReader("list"));
            while (true) {
                String line = br.readLine();
                if (line == null)
                    break;
                nameSurf.add(line);
            }

            br.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

}
