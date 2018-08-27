package projects.parcer;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import java.io.PrintWriter;

public class Parcing implements ParcingConstants{

    static Document document, underDocument;
    static Elements elements, underElements;
    static String idImage = "";
    static PrintWriter writer;

    public static void main(String[] args) throws Exception{
        document = Jsoup.connect(site1).get();
//        int energy = Integer.getInteger();
        System.out.println(document.attr("class","").attr("hero","energy_fight").text());
        if((int)1 > 0){

        }
    }
}
