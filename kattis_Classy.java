import java.util.Scanner;
import java.util.ArrayList;

class Classy
{
    static Scanner scan;
    static int people;
    static int cases;
    static ArrayList<String> classes;
    static String name;
    static String[] rank;
    static int[] nums;
    static String finalRanks[];

    public static void main(String[] args)
    {
        classes=new ArrayList<String>();
        scan=new Scanner(System.in);
        cases=scan.nextInt();
        while(cases>0)
        {
            people=scan.nextInt();
            int x=people;
            while(people>0)
            {
                Scanner scan2=new Scanner(System.in);
                name=scan2.nextLine();
                classes.add(name);
                people--;
            }

            ArrayList<ArrayList<String>> official=find_Class();
            for(int i=0; i<official.size(); i++)
            {
                for(int j=0; j<official.get(i).size(); j++)
                {
                    if(!(official.get(i).get(j).equals(null)))
                    {
                        System.out.println(official.get(i).get(j));
                    }
                }
            }
            System.out.println("==============================");
            cases--;
        }
    }

    static ArrayList<ArrayList<String>> find_Class()
    {
        int count=0;
        String[] names=new String[classes.size()];
        ArrayList< ArrayList<String>> lists =new ArrayList<ArrayList<String>>();
        ArrayList<String> one = new ArrayList<String>();
        lists.add(0, one);
        ArrayList<String> two = new ArrayList<String>();
        lists.add(0, two);
        ArrayList<String> three = new ArrayList<String>();
        lists.add(0, three);
        ArrayList<String> four = new ArrayList<String>();
        lists.add(four);
        ArrayList<String> zero = new ArrayList<String>();
        lists.add(0, zero);
        nums=new int[classes.size()];

        for(int i=0; i<classes.size(); i++)
        {
            for(int j=0; j<classes.get(i).length()-1 ;j++)
            {
                if(classes.get(i).substring(j,j+1).equals("-"))
                {
                    count++;
                }
            }
        }

        for(int i=0; i<classes.size(); i++)
        {
            for(int j=1; j<classes.get(i).length()-1; j++)
            {
                if(classes.get(i).substring(j,j+1).equals(":"))
                {
                    names[i]=(classes.get(i).substring(0,j));
                    rank=(classes.get(i).substring(j+2, classes.get(i).length()-6)).split("-",count+1);
                    j=classes.get(i).length()-2;
                }
            }

            nums[i]=find_Rank(rank);
        }
        
        for(int i=0; i<nums.length; i++)
        {
           lists.get(nums[i]).add(names[i]);
           //System.out.print(nums[i]+" ");
        }

        for(int i=0; i<lists.size(); i++)
        {
            lists.get(i).sort(null);
        }

        return lists;
    }

    static int find_Rank(String[] ranks)
    {	
    	/*for(int i=0; i<ranks.length; i++)
    	{
    		System.out.print(ranks[i]+" ");
    	}
    	*/
    	//System.out.println();
    	
        int mainNum=0;
        int checkL=0;
        int num=0;
        
        String theRank="lower";



        if(ranks.length!=1)
        {
        	for(int j=0; j<ranks.length-1; j++)
            {
                if(!(ranks[j].equals(ranks[j+1])))
                {
                    num=1;
                }
            }
        }
        
        else
        {
        	theRank=ranks[0]+"-middle";
        }

        if(num==1)
        {
            for(int j=0; j<ranks.length; j++)
            {
                if(ranks[j].equals("lower") && j!=0)
                {
                    theRank=ranks[j-1]+"-middle";
                    mainNum=check(theRank);
                    j=ranks.length-1;
                    checkL++;
                }
                
                else
                {
                	
                }
            }
            
            if(checkL==0)
            {
            	for(int j=0; j<ranks.length; j++)
            	{
            		if(ranks[j].equals("middle") && j!=0)
                    {
                        theRank=ranks[j-1]+"-middle";
                        mainNum=check(theRank);
                        j=ranks.length-1;
                    }
            		
            		else
            		{
            			
            		}
            	}
            }
            
            else
            {
            	
            }
            
            checkL=0;
        }

        else if(num==0)
        {
            mainNum=check(ranks[0]);
        }
        
        return mainNum;


    }

    static int check(String ranker)
    {
    	//System.out.print(ranker+" ");
        int count=0;

        String[] checker=new String[5];
        checker[0]="upper";
        checker[1]="upper-middle";
        checker[2]="middle-middle";
        checker[3]="middle";
        checker[4]="lower";

        for(int i=0; i<checker.length; i++)
        {
            if(checker[i].equals(ranker))
            {
               count=i; 
            }

        }

        return count;
    }


}