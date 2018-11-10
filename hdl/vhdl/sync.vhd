library ieee;
use ieee.std_logic_1164.all;

entity sync is
  generic (
    SYNC_DEPTH: natural := 2
  );
  port (
    i_clk: in std_logic;
    i_async: in std_logic;
    o_sync: out std_logic
  );
end entity sync;

architecture rtl of sync is

  signal sync_shift_reg: std_logic_vector(SYNC_DEPTH - 1 downto 0) :=
    (others => '0');

begin

  o_sync <= sync_shift_reg(sync_shift_reg'left);

  process (i_clk)
  begin
    if rising_edge(i_clk) then
      sync_shift_reg <= sync_shift_reg(SYNC_DEPTH - 2 downto 0) & i_async;
    end if;
  end process;

end architecture rtl;
