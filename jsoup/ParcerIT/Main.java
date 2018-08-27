package projects.ParcerIT;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.HashMap;


public class Main {

    private static Document document, underDocument;
    private static Elements elements, underElements;
    private static String idImage = "";
    private static PrintWriter writer;
    private static HashMap<String, String> site;
    private static ArrayList<String> nameSite;


    public static void main(String[] args) throws Exception {
        try {
            writer = new PrintWriter("optunion.csv", "Windows-1251");
            writer.println("\"Категория\";\"Ссылка\";\"Электронная почта\";\"Телефон\";\"Имя\";\"Адрес\"");
        } catch (Exception e) {
            System.out.println("Ошибка создания файла");
        }
        nameSite = new ArrayList<>();
        site = new HashMap<>();
        inputListSites();
        firstSite();
    }

    private static void inputListSites() {
        nameSite.add("optunion");
        site.put("optunion", "http://www.opt-union.ru/db/katalog-kompaniy.html");
    }


    private static void firstSite() {
        String category;
        try {
            document = Jsoup.connect("http://www.opt-union.ru/db/katalog-kompaniy.html").get();
            elements = document.select("ul");
            for (Element element : elements) {
                for (Element underElement : element.select("a[href]")) {
                    category = underElement.attr("title");
                    System.out.println(category + " - " + "http://www.opt-union.ru" + underElement.attr("href"));
                    giveStringsCategory("http://www.opt-union.ru" + underElement.attr("href"), category);
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
            System.out.println("Ошибка в парсинге opt-union");
        }
    }

    private static void giveStringsCategory(String category, String name) {
        String id, string = "", data_page = "-1";
        for (int i = 1; ; i++) {
            try {
                id = category + "?page=" + i;
                underDocument = Jsoup.connect(id).get();
                System.out.println(data_page);
                System.out.println(underDocument.select("li.active a").attr("data-page"));
                if (!data_page.equals(underDocument.select("li.active a").attr("data-page"))) {
                    data_page = underDocument.select("li.active a").attr("data-page");
                    System.out.println();
                    System.out.println("=======================");
                    System.out.println(data_page + " data_page");
                    System.out.println("====================");
                    for (Element element : underDocument.select(".comp-data-table")) {
//                    System.out.println(element.select("a[title]"));
//                    System.out.println(element.select("a[href]").attr("title"));
                        String address = "", phone = "", site = "", nameCompany = "";
                        nameCompany = element.select("a[title]").attr("title");

                        for (Element underElement : element.select(".dotted")) {
                            if (underElement.select(".left").text().equals("Регион:"))
                                address += underElement.select(".right").text() + ", ";
                            if (underElement.select(".left").text().equals("Страна:"))
                                address += underElement.select(".right").text() + ", ";
                            if (underElement.select(".left").text().equals("Город:"))
                                address += underElement.select(".right").text() + ", ";
                            if (underElement.select(".left").text().equals("Адрес:"))
                                address += underElement.select(".right").text();
                            if (underElement.select(".left").text().equals("Телефон:"))
                                phone += underElement.select(".right").text();
                            if (underElement.select(".left").text().equals("Интернет:"))
                                site += underElement.select(".right").text();

                        }
                        System.out.print(name + " | " + site + " | " + phone + " | " + nameCompany + " | " + address);
                        writer.println("\"" + name + "\";\"" + site + "\";\"" + "\";\"" + phone + "\";\"" + nameCompany + "\";\"" + address + "\"");
//                    writer.println(name+ "\t"  + site + "\t" + phone + "\t" + nameCompany + "\t" + address);
                    }
                }else {
                    break;
                }
            } catch (Exception e) {
                System.out.println("Ошибка в подпарсинге opt-union");
                System.out.println(e);
                break;
            }
        }
    }

    private static void writeCompany(Element underElement) {
        System.out.println();
        System.out.print(underElement.select(".left").text() + " ");
        System.out.print(underElement.select(".Right").text());
    }
}
