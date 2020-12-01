package day01;

import java.io.*;
import java.util.ArrayList;

public class Main
{

    private static final File input = new File("C:\\Dev\\projects\\advent-of-code\\java\\src\\day01\\input.txt");
    private static final ArrayList<Integer> list = new ArrayList<>();

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
                list.add(Integer.valueOf(line));
            }
            br.close();
        } catch (FileNotFoundException e) {
            System.out.println("File not found");
        } catch (IOException e) {
            e.printStackTrace();
        }

        for (int i = 0; i < list.size(); i++) {
            if (list.contains(2020 - list.get(i))) {
                result = list.get(i) * (2020 - list.get(i));
            }
        }
        return result;
    }

    private static int part2()
    {
        for (int i = 0; i < list.size(); i++) {
            for (int j = 0; j < list.size(); j++) {
                int a = list.get(i);
                int b = list.get(j);
                if (list.contains(2020 - a - b)) {
                    return (a * b * (2020 - a - b));
                }
            }
        }
        return 0;
    }
}
