library ieee;
use ieee.std_logic_1164.all;

entity dff is
  port (
    i_clk: in std_logic;
    i_reset: in std_logic;
    i_d: in std_logic;
    o_q: out std_logic
  );
end entity dff;

architecture rtl of dff is
begin

  process (i_clk, i_reset)
  begin
    if i_reset = '1' then
      o_q <= '0';
    elsif rising_edge(i_clk) then
      o_q <= i_d;
    end if;
  end process;

end architecture rtl;
