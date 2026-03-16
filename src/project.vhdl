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
   signal unused_inputs : std_logic_vector(4 downto 0);


begin  
   a1 <= ui_in(0) xor ui_in(1);  
   a2 <= ui_in(0) and ui_in(1);  
   a3 <= a1 and ui_in(2);  
   uo_out(0) <= a2 or a3;  
   uo_out(1) <= a1 xor ui_in(2);  

   uo_out(7 downto 2) <= (others => '0');
   uio_out <= (others => '0');
   uio_oe  <= (others => '0');
   unused_inputs <= ui_in(7 downto 3);


end structural;  
