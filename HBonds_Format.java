import java.io.FileInputStream;  
public class HBonds_Format {  
     public static void main(String args[]){    
          try{    
            FileInputStream fin=new FileInputStream("C:\\Users\venki\Argonne\HBondsJER.txt");    
            int i=0;    
            while((i=fin.read())!=-1){    
             System.out.print((char)i);    
            }    
            fin.close();    
          }catch(Exception e){System.out.println(e);}    
         }    
        }  