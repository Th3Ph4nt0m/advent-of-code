package day03;

import java.io.*;
import java.util.ArrayList;

public class Main
{
    private static final File input = new File("C:\\Dev\\projects\\advent-of-code\\java\\src\\day03\\input.txt");
    private static final ArrayList<String> list = new ArrayList<>();

    public static void main(String[] args)
    {
        System.out.println("Part 1: " + part1());
        System.out.println("Part 2: " + part2());
    }

    private static int part1()
    {
        String line;
        int result = 0;

        try {
            BufferedReader br = new BufferedReader(new FileReader(input));
            while ((line = br.readLine()) != null) {
                list.add(line);
            }
            br.close();
        } catch (FileNotFoundException e) {
            System.out.println("File not found");
        } catch (IOException e) {
            e.printStackTrace();
        }

        for(String s : list){

        }
    }

    private static int part2(){
        return 0;
    }
}
