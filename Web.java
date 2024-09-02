import java.awt.BorderLayout;
import javax.swing.JFrame;



class Web
{
    public Web()
    {
        JFrame frame=new JFrame();
        frame.setBounds(0,0,200,500);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new BorderLayout());
    }
}