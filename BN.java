import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;

public class BN{
    public static void main(String[] args) throws IOException {
        BufferedReader b = new BufferedReader(new InputStreamReader(System.in));
        String line[] = b.readLine().split("\\s");
        int n = Integer.parseInt(line[0]);
        line = b.readLine().split("\\s");
        ;
        Long arr_in[] = new Long[n];
        Long max_val = 0L;
        HashMap<Long, Integer> hm = new HashMap<>();
        int j=0;
        while(j < n) {
            arr_in[i] = Long.parseLong(line[i]);
            if(hm.containsKey(arr_in[i])) {
                hm.put(arr_in[i], hm.get(arr_in[i]) + 1);
            } else {
                hm.put(arr_in[i] , 1);
            }
            j=j+1;
        }
        for(Long lp : hm.keySet()) {
            max_val = Math.max(max_val, hm.get(lp));
        }
        System.out.println(max_val);
    }
}