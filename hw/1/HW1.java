package hw1;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class HW1 {
 class Col{

  public int N =0;
 }

 class Num extends Col {
   double sd = 0;
   double m2 = 0;
   double mu = 0;

  public double getSd() {
   return sd;
  }

  public double getMu() {
   return mu;
  }

  public void setMu(double mu) {
   this.mu = mu;
  }

  public void setSd(double sd) {
   this.sd = sd;
  }

  public  void addNum(int n)
  {
   N++;
   double delta = n - mu;
   mu += delta / N;
   double delta2 = n - mu;
   m2 += delta * delta2;
   sd = getStandardDeviation();
  }

  private int getStandardDeviation()
  {
   if (m2 < 0 || N < 2)
    return 0;
   return (int) Math.sqrt((m2 / (N - 1)));
  }


  public void removeNum(int n)
  {
  N--;
   if (N < 2) {
    sd = 0;
   }

   double delta = n - mu;
   mu -= delta/N;
   double delta2 = n - mu;
   m2 -= delta * delta2;
   sd = getStandardDeviation();
  }

 }

 class Sym extends Col{
 }

 class Some extends Col {
 }
public void getMeanAndSD( List nums, int n){
  Num num = new Num();
 List<Double> meansFwd  = new ArrayList<>();
 List<Double> sdsFwd  = new ArrayList<>();
 List<Double> meanDeltas  = new ArrayList<>();
 List<Double> sdDeltas  = new ArrayList<>();
 for(int i=1; i <= n; i++){
  num.addNum((int)nums.get(i-1));
  if(i >0 && i%10==0 ){
   meansFwd.add(num.mu);
   sdsFwd.add(num.sd);
  }
 }
 for(int i=n; i > 0; i--){
  if(i> 0 && i%10==0){
   meanDeltas.add(meansFwd.get((i/10)-1)-num.mu);
   sdDeltas.add(sdsFwd.get((i/10)-1)-num.sd);
  }
  num.removeNum((int)nums.get(i-1));
 }
 for(int i=0;i<sdDeltas.size();i++){
  if(sdDeltas.get(i) < .0001 && meanDeltas.get(i)<0.0001){
   System.out.println("Group " + i + " mean is "+meansFwd.get(i) +" standard deviation is "+ sdsFwd.get(i));
  }
 }
}
public static void main(String[] args){
  int n=100;

 List<Integer> numbers  = new ArrayList<>();
 Random random = new Random();
 for(int i=0;i<n;i++)
  numbers.add(random.nextInt(Integer.MAX_VALUE));
 HW1 hw = new HW1();
 hw.getMeanAndSD(numbers, n);
}

}

