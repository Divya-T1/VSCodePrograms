import javax.swing.GroupLayout;
import javax.swing.JFrame;
import javax.swing.JPanel;

public class Python_Class_Intro
{
    static JFrame frame;
    static JPanel panel1;
    public static void main(String[] args) 
    {
        frame=new JFrame();
        frame.setBounds(200, 250, 350, 350);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new BorderLayout(2,2));
        frame.setVisible(true);

        panel1=new JPanel();
        frame.add(panel1, BorderLayout.CENTER);
        //Python_Class_Intro intro=new Python_Class_Intro();
    }

    /*public Python_Class_Intro()
    {
        
        
    }*/
}