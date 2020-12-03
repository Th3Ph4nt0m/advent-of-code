package day02;

import java.io.*;
import java.util.ArrayList;

public class Main
{

    private static final File input = new File("C:\\Dev\\projects\\advent-of-code\\java\\src\\day02\\input.txt");
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

        for (String s : list) {
            String[] split = s.split(": ");
            String[] policy = split[0].split(" ");
            char letter = policy[1].toCharArray()[0];
            String[] counts = policy[0].split("-");
            int min = Integer.parseInt(counts[0]);
            int max = Integer.parseInt(counts[1]);
            String pw = split[1];

            int count = countChar(pw, letter);

            if (count <= max && count >= min) {
                result++;
            }
        }
        return result;
    }

    private static int part2()
    {
        int result = 0;

        for (String s : list) {
            String[] split = s.split(": ");
            String[] policy = split[0].split(" ");
            char letter = policy[1].toCharArray()[0];
            String[] counts = policy[0].split("-");
            int min = Integer.parseInt(counts[0]);
            int max = Integer.parseInt(counts[1]);
            String pw = split[1];

            if((pw.charAt(min - 1) == letter) != (pw.charAt(max - 1) == letter)){
                result++;
            }
        }
        return result;
    }


    private static int countChar(CharSequence seq, char letter)
    {
        int count = 0;
        for (int i = 0; i < seq.length(); i++) {
            if (letter == seq.charAt(i)) {
                count += 1;
            }
        }
        return count;
    }
}
