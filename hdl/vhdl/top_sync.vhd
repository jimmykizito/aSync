library ieee;
use ieee.std_logic_1164.all;

--! Simple synchroniser formed by chaining flip-flops.
entity top_sync is
  generic (
    SYNC_DEPTH: natural := 2
  );
  port (
    i_clk: in std_logic;
    i_async: in std_logic;
    o_sync: out std_logic
  );
end entity top_sync;

architecture rtl of top_sync is

  -- Submodule instantiation
  component sync
    generic (
      SYNC_DEPTH: natural := 2
    );
    port (
      i_clk: in std_logic;
      i_async: in std_logic;
      o_sync: out std_logic
    );
  end component sync;

begin

  u_sync: sync
    generic map (
      SYNC_DEPTH => SYNC_DEPTH
    )
    port map (
      -- i|io|o_port_name => port|signal,
      i_clk => i_clk,
      i_async => i_async,
      o_sync => o_sync
    );

end architecture rtl;
