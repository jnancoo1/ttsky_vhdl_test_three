library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity tt_um_example is
    port (
        ui_in   : in  std_logic_vector(7 downto 0);
        uo_out  : out std_logic_vector(7 downto 0);
        uio_in  : in  std_logic_vector(7 downto 0);
        uio_out : out std_logic_vector(7 downto 0);
        uio_oe  : out std_logic_vector(7 downto 0);
        ena     : in  std_logic;
        clk     : in  std_logic;
        rst_n   : in  std_logic
    );
end tt_um_example;

architecture structural of tt_um_example is  

   signal a1, a2, a3: std_logic;  

begin  
   a1 <= u1_in(0) xor u1_in(1);  
   a2 <= u1_in(0) and u1_in(1);  
   a3 <= a1 and u1_in(2);  
   uo_out(0) <= a2 or a3;  
   uo_out(1) <= a1 xor u1_in(2);  

end structural;  
