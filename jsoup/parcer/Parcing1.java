package projects.parcer;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import java.io.PrintWriter;

public class Parcing1 implements ParcingConstants{

    static Document document, underDocument;
    static Elements elements, underElements;
    static String idImage = "";
    static PrintWriter writer;

    public static void main(String[] args) throws Exception{
        writer = new PrintWriter("index.html", "UTF-8");
        for (int i = 0; i < 221; i +=42){
            document = Jsoup.connect(site+i).get();
            elements = document.select("img");
            for (Element element : elements) {
                idImage = underSite + element.attr("alt").replaceAll("Image: ","");
                underDocument = Jsoup.connect(idImage).get();
//                underElements = underDocument.select("img");
                underElements = underDocument.select("img");
                for (Element underElement : underElements) {
                    try{
                        if(Integer.parseInt(underElement.attr("data-original-width"))<100) {
                            System.out.println(underElement.attr("id", "image"));
                            writer.println(underElement.attr("id", "image"));
                        }
                    }catch (Exception e){
                        System.out.println(e.getMessage());
                        System.out.println("error");
                    }
                }

            }
        }
    }
}
