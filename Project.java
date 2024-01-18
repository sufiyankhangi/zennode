// this code is based on conditional functioning
// code is setup for direct run you just type inputs which is required or ask by prompt
import java.util.Scanner;
public class Project {
    public static void main(String []args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter Quantity For Product A ($20) :");
        int a = sc.nextInt();
        System.out.print("if you want to wrap these (Y/N):");
        String aw = sc.next();
        int ac =0;
        if(aw.equals("y")||aw.equals("Y")){
            ac =a;
        }
        //        input for product a
        System.out.print("Enter Quantity For Product B ($40) :");
        int b = sc.nextInt();
        System.out.print("if you want to wrap these (Y/N):");
        String bw = sc.next();
        int bc =0;
        if(bw.equals("y")||bw.equals("Y")){
            bc =b;
        }
        //     inputs for product b
        System.out.print("Enter Quantity For Product C ($50) :");
        int c = sc.nextInt();
        System.out.print("if you want to wrap these (Y/N):");
        String cw = sc.next();
        int cc =0;
        if(cw.equals("y")||cw.equals("Y")){
            cc =c;
        }
        //     input for product c

        //     -------------------- calculation / finding best discount -----------------
        int cart = 20*a +40*b + 50*c ; 
        double discount = 0; 
        String distype ="No_Discount_Aypplicable";


        if(cart>200){
            discount =10;
            distype = "Flat_10_Discount";
        }

        if(((a+b+c) >30) && (a>15 || b>15 || c>15)){
            if(c>15){
                discount = Math.max(discount,(c-15)*50*.5);
            }
            if(b>15){
                discount = Math.max(discount,(b-15)*40*.5);
            }
            if(a>15){
                discount = Math.max(discount,(a-15)*20*.5);
            }
            distype = "Tiered_50_Discount";
        }

        if(a>10 || b>10 || c>10){
            if(c>10){
                discount = Math.max(discount,c*50*.05);
            }
            if(b>10){
                discount = Math.max(discount,b*40*.05);
            }
            if(a>10){
                discount = Math.max(discount,a*20*.05);
            }
            distype = "Bulk_5_Discount";
        }

        if((a+b+c)>20){
            if(discount<cart*.1){
                discount = cart*.1;
                distype= "Bulk_10_Discount";
            }
        }

        //   ------------- shipping and gift wrap fee -----------------

        int total_Units = a+b+c;
        int ten_units_packs = total_Units/10;
        int not_ten_packs = total_Units%10;
        int ship_fee = ten_units_packs*5;
        if(not_ten_packs>0){
            ship_fee+=5;
        }
        int gift_wrp_fee = ac+bc+cc;


        //      ------------Printing statements--------------

System.out.println(" ");
System.out.println("======================================");
System.out.println("               Billing");
System.out.println("======================================");
System.out.println("Product_Name : Quantity : Total_Amount");
System.out.println("Product_A : "+ a + " :  $"+ 20*a);
System.out.println("Product_B : "+ b + " :  $"+ 40*b);
System.out.println("Product_C : "+ c + " :  $"+ 50*c);
System.out.println("-------------------------------------");
System.out.println("Subtotal :  $" + cart);
System.out.println("-------------------------------------");
System.out.println("Discount_Name_Applied : " + distype);
System.out.println("Discount_Amount :   - $"+ discount);
System.out.println("-------------------------------------");
System.out.println("Shipping_Amount :   $"+ ship_fee);
System.out.println("Gift_Wrap_Amount :   $"+ gift_wrp_fee);
System.out.println("======================================");
System.out.println("Total_Amount :   $"+ (cart-discount+ship_fee+gift_wrp_fee));
System.out.println("======================================");
    } 
}
