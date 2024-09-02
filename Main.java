public class Main {
    
    public static void main(String[] args) {
        Main obj=new Main();
        obj.processNumbers("1\n 2 \n4\n");
    }

    void processNumbers(String nums)
    {
        int index = 0;
        int count = 0;
        int sum = 0;
        int ctEven = 0;
        int ctOdd = 0;

        while(index<nums.length())
        {
            int y=nums.indexOf("\n", index);
            if(y==-1)
            {
                y=nums.length();
            }
            for(int i=index; i<y; i++)
            {
                int ct=0;
                String num="";
                int x=1;
                if(!(nums.substring(i, i+x).equals(" ")))
                {
                    while(!(nums.substring(i, i+x).equals(" ")) && (i+x)<y)
                    {
                        num=num+nums.substring(i, i+x);
                        //System.out.println(num);
                        i++;
                        ct++;
                    }

                    if(ct>0)
                    {
                        i--;
                    }
                    
                    count++;

                    if(!num.isEmpty())
                    {
                        sum+=Integer.parseInt(num);

                        if(Integer.parseInt(num)%2==0)
                        {
                            ctEven++;
                        }

                        else
                        {
                            ctOdd++;
                        }

                    }
                }
            }

            index=y+1;
        }


        System.out.println("Count: "+count);
        System.out.println("Sum: "+ sum);
        System.out.println("Count Even: "+ctEven);
        System.out.println("Count Odd: "+ctOdd);
        System.out.printf("Average: %.1f", Double.valueOf(sum)/count);
    
    }



}
