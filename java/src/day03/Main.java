package day03;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.util.List;

public class Main
{
    public static void main(String[] args)
    {
        System.out.println("Part 1: " + solve(3, 1));

        long result = 1;
        result *= solve(1, 1);
        result *= solve(3, 1);
        result *= solve(5, 1);
        result *= solve(7, 1);
        result *= solve(1, 2);
        System.out.println("Part 2: " + result);
    }


    private static long solve(int right, int down){
        try {
            List<String> lines = Files.readAllLines(new File("C:\\Dev\\projects\\advent-of-code\\java\\src\\day03\\input.txt").toPath());
            int posR = 1 + right, posDown = down;
            int trees = 0;
            for(int i = down; i < lines.size(); i+= down){
                String line = lines.get(i);
                char c = line.charAt(posR - 1);
                if(c == '#'){
                    trees++;
                }
                posDown += down;
                posR = posR + right;
                if(posR > line.length()){
                    posR = posR % line.length();
                }
            }
            return trees;
        } catch (IOException e) {
            e.printStackTrace();
            return -1;
        }
    }
}
