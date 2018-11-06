library ieee;
use ieee.std_logic_1164.all;

--! Module description.
entity top_sync is
  -- generic (
    -- _PARAM: type := DEFAULT_VALUE;
  -- );
  port (
    -- i|io|o_port_name: in|inout|out type;
    i_clk: in std_logic;
    i_reset: in std_logic;
    i_d: in std_logic;
    o_q: out std_logic
  );
end entity top_sync;

architecture rtl of top_sync is

  -- Submodule instantiation
  component dff
    -- generic (
      -- _PARAM: type := DEFAULT_VALUE;
    -- );
    port (
      -- i|io|o_port_name: in|inout|out type;
      i_clk: in std_logic;
      i_reset: in std_logic;
      i_d: in std_logic;
      o_q: out std_logic
    );
  end component;

begin

  u_dff: dff
    -- generic map (
      -- _PARAM => VALUE,
    -- )
    port map (
      -- i|io|o_port_name => port|signal,
      i_clk => i_clk,
      i_reset => i_reset,
      i_d => i_d,
      o_q => o_q
    );

end architecture rtl;
