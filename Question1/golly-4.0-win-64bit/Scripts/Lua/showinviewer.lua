-- Launch LifeViewer in the default browser with the current Golly pattern
--
-- Author:
--   Chris Rowett (crowett@gmail.com)

local g = golly()
local gp = require "gplus"

-- name of this script
local myname = "showinviewer.lua"

-- width and height of the LifeViewer canvas in pixels
local viewerwidth = 800
local viewerheight = 700

-- folder name for LifeViewer files
local lifeviewerfolder = "lifeviewer"

-- name of launch HTML file
local launchfilename = "launch.html"

-- name of LifeViewer Javascript plugin
local lifeviewerfilename = "lv-plugin.js"

-- download URL for latest LifeViewer build
local lifeviewerdownload = "https://lazyslug.com/lifeview/plugin/js/release/"

-- maximum width, height and number of cells of patterns for LifeViewer
local maxwd = 8127
local maxht = 8127
local maxcells = 1000000  -- just for performance when loading large RLE

-- path separator
local pathsep = g.getdir("app"):sub(-1)

--------------------------------------------------------------------------------

local function getJvNruletext(rule)
    local ruletext = ""
    if rule == "JvN29" then
        ruletext = [[
@RULE JvN29
# Transitions rules for John von Neumann's 29 state CA.
@TREE
num_states=29
num_neighbors=4
num_nodes=67
1 0 2 4 6 8 12 18 20 9 9 10 11 12 9 10 11 12 17 18 19 20 17 18 19 20 25 27 25 27
1 1 3 5 7 11 17 19 25 10 13 14 15 12 13 14 15 12 0 0 0 0 0 0 0 0 26 28 26 28
1 1 3 5 7 11 17 19 25 10 0 0 0 0 0 0 0 0 21 22 23 20 21 22 23 20 0 0 0 0
1 0 2 4 6 8 12 18 20 9 13 14 15 12 13 14 15 12 21 22 23 20 21 22 23 20 25 27 25 27
2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 2 0 0 0 0 3 3
1 1 3 5 7 11 17 19 25 10 13 14 15 12 13 14 15 12 0 0 0 0 0 0 0 0 25 27 25 27
2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 5 0 0 0 0 0 0 0 2 0 0 0 0 3 3
1 1 3 5 7 11 17 19 25 10 9 14 15 16 9 14 15 16 0 0 0 0 0 0 0 0 26 28 26 28
1 1 3 5 7 11 17 19 25 10 9 14 15 16 9 14 15 16 0 0 0 0 0 0 0 0 25 27 25 27
1 1 3 5 7 11 17 19 25 10 13 14 15 16 13 14 15 16 0 0 0 0 0 0 0 0 26 28 26 28
1 1 3 5 7 11 17 19 25 10 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
2 7 7 7 7 7 7 7 7 7 7 8 7 7 7 9 7 7 7 7 7 7 7 10 7 7 7 7 9 9
1 1 3 5 7 11 17 19 25 10 0 0 0 0 0 0 0 0 17 22 23 24 17 22 23 24 0 0 0 0
1 1 3 5 7 11 17 19 25 10 0 0 0 0 0 0 0 0 21 22 23 24 21 22 23 24 0 0 0 0
2 12 12 12 12 12 12 12 12 12 12 12 12 12 12 10 12 12 12 12 12 12 12 13 12 12 12 12 13 13
1 0 2 4 6 8 12 18 20 9 9 14 15 16 9 14 15 16 17 22 23 24 17 22 23 24 25 27 25 27
1 0 2 4 6 8 12 18 20 9 13 14 15 16 13 14 15 16 21 22 23 24 21 22 23 24 25 27 25 27
2 15 15 15 15 15 15 15 15 15 15 15 15 15 15 9 15 15 15 15 15 15 15 13 15 15 15 15 16 16
3 4 4 4 4 4 4 4 4 4 4 4 6 4 4 4 11 4 4 4 4 4 4 4 14 4 4 4 17 17
1 1 3 5 7 11 17 19 25 10 13 14 15 16 13 14 15 16 0 0 0 0 0 0 0 0 25 27 25 27
2 8 8 8 8 8 8 8 8 8 8 8 8 8 8 19 8 8 8 8 8 8 8 10 8 8 8 8 19 19
2 15 15 15 15 15 15 15 15 15 15 15 15 15 15 19 15 15 15 15 15 15 15 13 15 15 15 15 16 16
3 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 20 6 6 6 6 6 6 6 14 6 6 6 21 21
1 1 3 5 7 11 17 19 25 10 13 14 11 16 13 14 11 16 0 0 0 0 0 0 0 0 26 28 26 28
1 1 3 5 7 11 17 19 25 10 13 14 11 16 13 14 11 16 0 0 0 0 0 0 0 0 25 27 25 27
2 23 23 23 23 23 23 23 23 23 23 24 23 23 23 9 23 23 23 23 23 23 23 10 23 23 23 23 9 9
2 24 24 24 24 24 24 24 24 24 24 24 24 24 24 19 24 24 24 24 24 24 24 10 24 24 24 24 19 19
2 9 9 9 9 9 9 9 9 9 9 19 9 9 9 9 9 9 9 9 9 9 9 10 9 9 9 9 9 9
2 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10
3 25 25 25 25 25 25 25 25 25 25 25 26 25 25 25 27 25 25 25 25 25 25 25 28 25 25 25 27 27
1 1 3 5 7 11 17 19 25 10 0 0 0 0 0 0 0 0 21 22 19 24 21 22 19 24 0 0 0 0
2 30 30 30 30 30 30 30 30 30 30 30 30 30 30 10 30 30 30 30 30 30 30 13 30 30 30 30 13 13
2 13 13 13 13 13 13 13 13 13 13 13 13 13 13 10 13 13 13 13 13 13 13 13 13 13 13 13 13 13
3 31 31 31 31 31 31 31 31 31 31 31 31 31 31 31 28 31 31 31 31 31 31 31 32 31 31 31 32 32
1 0 2 4 6 8 12 18 20 9 13 14 11 16 13 14 11 16 21 22 19 24 21 22 19 24 25 27 25 27
2 34 34 34 34 34 34 34 34 34 34 34 34 34 34 9 34 34 34 34 34 34 34 13 34 34 34 34 16 16
2 34 34 34 34 34 34 34 34 34 34 34 34 34 34 19 34 34 34 34 34 34 34 13 34 34 34 34 16 16
2 16 16 16 16 16 16 16 16 16 16 16 16 16 16 9 16 16 16 16 16 16 16 13 16 16 16 16 16 16
3 35 35 35 35 35 35 35 35 35 35 35 36 35 35 35 27 35 35 35 35 35 35 35 32 35 35 35 37 37
4 18 18 18 18 18 18 18 18 18 22 18 18 18 29 18 18 18 18 18 18 18 33 18 18 18 18 18 38 38
2 19 19 19 19 19 19 19 19 19 19 19 19 19 19 19 19 19 19 19 19 19 19 10 19 19 19 19 19 19
3 26 26 26 26 26 26 26 26 26 26 26 26 26 26 26 40 26 26 26 26 26 26 26 28 26 26 26 40 40
2 16 16 16 16 16 16 16 16 16 16 16 16 16 16 19 16 16 16 16 16 16 16 13 16 16 16 16 16 16
3 36 36 36 36 36 36 36 36 36 36 36 36 36 36 36 40 36 36 36 36 36 36 36 32 36 36 36 42 42
4 22 22 22 22 22 22 22 22 22 22 22 22 22 41 22 22 22 22 22 22 22 33 22 22 22 22 22 43 43
1 1 3 5 7 11 17 19 25 10 13 10 15 16 13 10 15 16 0 0 0 0 0 0 0 0 26 28 26 28
1 1 3 5 7 11 17 19 25 10 13 10 15 16 13 10 15 16 0 0 0 0 0 0 0 0 25 27 25 27
2 45 45 45 45 45 45 45 45 45 45 46 45 45 45 9 45 45 45 45 45 45 45 10 45 45 45 45 9 9
2 46 46 46 46 46 46 46 46 46 46 46 46 46 46 19 46 46 46 46 46 46 46 10 46 46 46 46 19 19
3 47 47 47 47 47 47 47 47 47 47 47 48 47 47 47 27 47 47 47 47 47 47 47 28 47 47 47 27 27
3 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 40 48 48 48 48 48 48 48 28 48 48 48 40 40
3 27 27 27 27 27 27 27 27 27 27 27 40 27 27 27 27 27 27 27 27 27 27 27 28 27 27 27 27 27
3 28 28 28 28 28 28 28 28 28 28 28 28 28 28 28 28 28 28 28 28 28 28 28 28 28 28 28 28 28
4 49 49 49 49 49 49 49 49 49 50 49 49 49 51 49 49 49 49 49 49 49 52 49 49 49 49 49 51 51
1 1 3 5 7 11 17 19 25 10 0 0 0 0 0 0 0 0 21 18 23 24 21 18 23 24 0 0 0 0
2 54 54 54 54 54 54 54 54 54 54 54 54 54 54 10 54 54 54 54 54 54 54 13 54 54 54 54 13 13
3 55 55 55 55 55 55 55 55 55 55 55 55 55 55 55 28 55 55 55 55 55 55 55 32 55 55 55 32 32
3 32 32 32 32 32 32 32 32 32 32 32 32 32 32 32 28 32 32 32 32 32 32 32 32 32 32 32 32 32
4 56 56 56 56 56 56 56 56 56 56 56 56 56 52 56 56 56 56 56 56 56 57 56 56 56 56 56 57 57
1 0 2 4 6 8 12 18 20 9 13 10 15 16 13 10 15 16 21 18 23 24 21 18 23 24 25 27 25 27
2 59 59 59 59 59 59 59 59 59 59 59 59 59 59 9 59 59 59 59 59 59 59 13 59 59 59 59 16 16
2 59 59 59 59 59 59 59 59 59 59 59 59 59 59 19 59 59 59 59 59 59 59 13 59 59 59 59 16 16
3 60 60 60 60 60 60 60 60 60 60 60 61 60 60 60 27 60 60 60 60 60 60 60 32 60 60 60 37 37
3 61 61 61 61 61 61 61 61 61 61 61 61 61 61 61 40 61 61 61 61 61 61 61 32 61 61 61 42 42
3 37 37 37 37 37 37 37 37 37 37 37 42 37 37 37 27 37 37 37 37 37 37 37 32 37 37 37 37 37
4 62 62 62 62 62 62 62 62 62 63 62 62 62 51 62 62 62 62 62 62 62 57 62 62 62 62 62 64 64
5 39 39 39 39 39 39 39 39 39 39 39 39 44 39 39 39 53 39 39 39 39 39 39 39 58 39 39 65 65
        ]]
    elseif rule == "Nobili32" then
        ruletext = [[
@RULE Nobili32
# Transitions rules for Nobili32 / EVN - extended von Neumann CA
#
# Renato Nobili <renato.nobili@pd.infn.it>
# http://www.pd.infn.it/~rnobili/au_cell/
@TREE

num_states=32
num_neighbors=4
num_nodes=118
1 0 2 4 6 8 12 18 20 9 9 10 11 12 9 10 11 12 17 18 19 20 17 18 19 20 25 26 27 28 25 25 25
1 0 2 4 6 8 12 18 20 9 9 10 11 12 9 10 11 12 17 18 19 20 17 18 19 20 25 27 25 27 25 25 25
1 1 3 5 7 11 17 19 25 10 13 14 15 12 13 14 15 12 0 0 0 0 0 0 0 0 26 28 26 28 26 26 26
1 1 3 5 7 11 17 19 25 10 0 0 0 0 0 0 0 0 21 22 23 20 21 22 23 20 0 0 0 0 0 0 0
1 0 2 4 6 8 12 18 20 9 13 14 15 12 13 14 15 12 21 22 23 20 21 22 23 20 25 26 27 28 25 25 25
2 0 0 0 0 0 0 0 0 0 1 0 1 1 1 2 1 1 1 0 1 1 1 3 1 1 0 0 4 4 0 4 4
1 0 2 4 6 8 12 18 20 9 13 14 15 12 13 14 15 12 21 22 23 20 21 22 23 20 25 27 25 27 25 25 25
2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 1 1 1 1 1 1 1 3 1 1 1 1 6 6 1 6 6
1 1 3 5 7 11 17 19 25 10 13 14 15 12 13 14 15 12 0 0 0 0 0 0 0 0 25 26 27 28 25 25 25
2 0 0 0 0 0 0 0 0 0 1 0 1 1 1 8 1 1 1 0 1 1 1 3 1 1 0 0 4 4 0 4 4
1 1 3 5 7 11 17 19 25 10 9 14 15 16 9 14 15 16 0 0 0 0 0 0 0 0 26 28 26 28 26 26 26
1 1 3 5 7 11 17 19 25 10 9 14 15 16 9 14 15 16 0 0 0 0 0 0 0 0 25 26 27 28 25 25 25
1 1 3 5 7 11 17 19 25 10 13 14 15 16 13 14 15 16 0 0 0 0 0 0 0 0 26 28 26 28 26 26 26
1 1 3 5 7 11 17 19 25 10 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
2 10 10 10 10 10 10 10 10 10 10 11 10 10 10 12 10 10 10 10 10 10 10 13 10 10 10 10 12 12 10 12 12
1 1 3 5 7 11 17 19 25 10 0 0 0 0 0 0 0 0 17 22 23 24 17 22 23 24 0 0 0 0 0 0 0
1 1 3 5 7 11 17 19 25 10 0 0 0 0 0 0 0 0 21 22 23 24 21 22 23 24 0 0 0 0 0 0 0
2 15 15 15 15 15 15 15 15 15 15 15 15 15 15 13 15 15 15 15 15 15 15 16 15 15 15 15 16 16 15 16 16
1 0 2 4 6 8 12 18 20 9 9 14 15 16 9 14 15 16 17 22 23 24 17 22 23 24 25 26 27 28 25 25 25
1 0 2 4 6 8 12 18 20 9 9 14 15 16 9 14 15 16 17 22 23 24 17 22 23 24 25 27 25 27 25 25 25
1 0 2 4 6 8 12 18 20 9 13 14 15 16 13 14 15 16 21 22 23 24 21 22 23 24 25 26 27 28 25 25 25
2 18 18 18 18 18 18 18 18 18 19 18 19 19 19 12 19 19 19 18 19 19 19 16 19 19 18 18 20 20 18 20 20
3 5 5 5 5 5 5 5 5 5 7 7 9 7 7 7 14 7 7 7 5 7 7 7 17 7 5 5 21 21 21 5 21
1 1 3 5 7 11 17 19 25 10 13 14 15 12 13 14 15 12 0 0 0 0 0 0 0 0 25 27 25 27 25 25 25
2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 23 1 1 1 1 1 1 1 3 1 1 1 1 6 6 1 6 6
1 1 3 5 7 11 17 19 25 10 9 14 15 16 9 14 15 16 0 0 0 0 0 0 0 0 25 27 25 27 25 25 25
1 1 3 5 7 11 17 19 25 10 13 14 15 16 13 14 15 16 0 0 0 0 0 0 0 0 25 26 27 28 25 25 25
2 11 11 11 11 11 11 11 11 11 25 11 25 25 25 26 25 25 25 11 25 25 25 13 25 25 11 11 26 26 11 26 26
2 18 18 18 18 18 18 18 18 18 19 18 19 19 19 26 19 19 19 18 19 19 19 16 19 19 18 18 20 20 18 20 20
3 9 9 9 9 9 9 9 9 9 24 24 9 24 24 24 27 24 24 24 9 24 24 24 17 24 9 9 28 28 28 9 28
2 10 10 10 10 10 10 10 10 10 10 25 10 10 10 12 10 10 10 10 10 10 10 13 10 10 10 10 12 12 10 12 12
1 0 2 4 6 8 12 18 20 9 13 14 15 16 13 14 15 16 21 22 23 24 21 22 23 24 25 27 25 27 25 25 25
2 19 19 19 19 19 19 19 19 19 19 19 19 19 19 12 19 19 19 19 19 19 19 16 19 19 19 19 31 31 19 31 31
3 7 7 7 7 7 7 7 7 7 7 7 24 7 7 7 30 7 7 7 7 7 7 7 17 7 7 7 32 32 32 7 32
1 1 3 5 7 11 17 19 25 10 13 14 11 16 13 14 11 16 0 0 0 0 0 0 0 0 26 28 26 28 26 26 26
1 1 3 5 7 11 17 19 25 10 13 14 11 16 13 14 11 16 0 0 0 0 0 0 0 0 25 26 27 28 25 25 25
2 34 34 34 34 34 34 34 34 34 34 35 34 34 34 12 34 34 34 34 34 34 34 13 34 34 34 34 12 12 34 12 12
1 1 3 5 7 11 17 19 25 10 13 14 11 16 13 14 11 16 0 0 0 0 0 0 0 0 25 27 25 27 25 25 25
2 34 34 34 34 34 34 34 34 34 34 37 34 34 34 12 34 34 34 34 34 34 34 13 34 34 34 34 12 12 34 12 12
2 35 35 35 35 35 35 35 35 35 37 35 37 37 37 26 37 37 37 35 37 37 37 13 37 37 35 35 26 26 35 26 26
2 12 12 12 12 12 12 12 12 12 12 26 12 12 12 12 12 12 12 12 12 12 12 13 12 12 12 12 12 12 12 12 12
2 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13
3 36 36 36 36 36 36 36 36 36 38 38 39 38 38 38 40 38 38 38 36 38 38 38 41 38 36 36 40 40 40 36 40
1 1 3 5 7 11 17 19 25 10 0 0 0 0 0 0 0 0 21 22 19 24 21 22 19 24 0 0 0 0 0 0 0
2 43 43 43 43 43 43 43 43 43 43 43 43 43 43 13 43 43 43 43 43 43 43 16 43 43 43 43 16 16 43 16 16
2 16 16 16 16 16 16 16 16 16 16 16 16 16 16 13 16 16 16 16 16 16 16 16 16 16 16 16 16 16 16 16 16
3 44 44 44 44 44 44 44 44 44 44 44 44 44 44 44 41 44 44 44 44 44 44 44 45 44 44 44 45 45 45 44 45
1 0 2 4 6 8 12 18 20 9 13 14 11 16 13 14 11 16 21 22 19 24 21 22 19 24 25 26 27 28 25 25 25
1 0 2 4 6 8 12 18 20 9 13 14 11 16 13 14 11 16 21 22 19 24 21 22 19 24 25 27 25 27 25 25 25
2 47 47 47 47 47 47 47 47 47 48 47 48 48 48 12 48 48 48 47 48 48 48 16 48 48 47 47 20 20 47 20 20
2 48 48 48 48 48 48 48 48 48 48 48 48 48 48 12 48 48 48 48 48 48 48 16 48 48 48 48 31 31 48 31 31
2 47 47 47 47 47 47 47 47 47 48 47 48 48 48 26 48 48 48 47 48 48 48 16 48 48 47 47 20 20 47 20 20
2 20 20 20 20 20 20 20 20 20 31 20 31 31 31 12 31 31 31 20 31 31 31 16 31 31 20 20 20 20 20 20 20
3 49 49 49 49 49 49 49 49 49 50 50 51 50 50 50 40 50 50 50 49 50 50 50 45 50 49 49 52 52 52 49 52
4 22 22 22 22 22 22 22 22 22 29 33 33 33 42 33 33 33 22 33 33 33 46 33 33 33 22 22 53 53 53 22 53
1 0 2 4 6 8 12 18 20 9 9 10 11 12 9 10 11 12 17 18 19 20 17 18 19 20 25 25 25 25 25 25 25
1 1 3 5 7 11 17 19 25 10 13 14 15 12 13 14 15 12 0 0 0 0 0 0 0 0 30 30 30 30 30 30 30
2 1 1 1 1 1 1 1 1 1 1 55 1 1 1 56 1 1 1 1 1 1 1 3 1 1 1 1 6 6 1 6 6
1 1 3 5 7 11 17 19 25 10 13 14 15 16 13 14 15 16 0 0 0 0 0 0 0 0 25 27 25 27 25 25 25
2 25 25 25 25 25 25 25 25 25 25 25 25 25 25 58 25 25 25 25 25 25 25 13 25 25 25 25 58 58 25 58 58
2 19 19 19 19 19 19 19 19 19 19 19 19 19 19 58 19 19 19 19 19 19 19 16 19 19 19 19 31 31 19 31 31
3 24 24 24 24 24 24 24 24 24 57 57 24 57 57 57 59 57 57 57 24 57 57 57 17 57 24 24 60 60 60 24 60
1 1 3 5 7 11 17 19 25 10 9 14 15 16 9 14 15 16 0 0 0 0 0 0 0 0 29 29 29 29 29 29 29
1 1 3 5 7 11 17 19 25 10 13 14 15 16 13 14 15 16 0 0 0 0 0 0 0 0 31 31 31 31 31 31 31
2 10 10 10 10 10 10 10 10 10 10 62 10 10 10 63 10 10 10 10 10 10 10 13 10 10 10 10 12 12 10 12 12
3 7 7 7 7 7 7 7 7 7 7 7 57 7 7 7 64 7 7 7 7 7 7 7 17 7 7 7 32 32 32 7 32
1 1 3 5 7 11 17 19 25 10 13 14 11 16 13 14 11 16 0 0 0 0 0 0 0 0 29 29 29 29 29 29 29
2 34 34 34 34 34 34 34 34 34 34 66 34 34 34 63 34 34 34 34 34 34 34 13 34 34 34 34 12 12 34 12 12
2 37 37 37 37 37 37 37 37 37 37 37 37 37 37 58 37 37 37 37 37 37 37 13 37 37 37 37 58 58 37 58 58
2 12 12 12 12 12 12 12 12 12 12 58 12 12 12 12 12 12 12 12 12 12 12 13 12 12 12 12 12 12 12 12 12
3 38 38 38 38 38 38 38 38 38 67 67 68 67 67 67 69 67 67 67 38 67 67 67 41 67 38 38 69 69 69 38 69
2 48 48 48 48 48 48 48 48 48 48 48 48 48 48 58 48 48 48 48 48 48 48 16 48 48 48 48 31 31 48 31 31
2 31 31 31 31 31 31 31 31 31 31 31 31 31 31 12 31 31 31 31 31 31 31 16 31 31 31 31 31 31 31 31 31
3 50 50 50 50 50 50 50 50 50 50 50 71 50 50 50 69 50 50 50 50 50 50 50 45 50 50 50 72 72 72 50 72
4 33 33 33 33 33 33 33 33 33 61 65 65 65 70 65 65 65 33 65 65 65 46 65 65 65 33 33 73 73 73 33 73
2 1 1 1 1 1 1 1 1 1 55 1 55 55 55 23 55 55 55 1 55 55 55 3 55 55 1 1 6 6 1 6 6
3 9 9 9 9 9 9 9 9 9 75 75 9 75 75 75 27 75 75 75 9 75 75 75 17 75 9 9 28 28 28 9 28
2 25 25 25 25 25 25 25 25 25 62 25 62 62 62 58 62 62 62 25 62 62 62 13 62 62 25 25 58 58 25 58 58
3 24 24 24 24 24 24 24 24 24 24 24 75 24 24 24 77 24 24 24 24 24 24 24 17 24 24 24 60 60 60 24 60
2 37 37 37 37 37 37 37 37 37 66 37 66 66 66 58 66 66 66 37 66 66 66 13 66 66 37 37 58 58 37 58 58
2 26 26 26 26 26 26 26 26 26 58 26 58 58 58 26 58 58 58 26 58 58 58 13 58 58 26 26 26 26 26 26 26
3 39 39 39 39 39 39 39 39 39 79 79 39 79 79 79 80 79 79 79 39 79 79 79 41 79 39 39 80 80 80 39 80
2 20 20 20 20 20 20 20 20 20 31 20 31 31 31 26 31 31 31 20 31 31 31 16 31 31 20 20 20 20 20 20 20
3 51 51 51 51 51 51 51 51 51 71 71 51 71 71 71 80 71 71 71 51 71 71 71 45 71 51 51 82 82 82 51 82
4 29 29 29 29 29 29 29 29 29 76 78 78 78 81 78 78 78 29 78 78 78 46 78 78 78 29 29 83 83 83 29 83
1 1 3 5 7 11 17 19 25 10 13 10 15 16 13 10 15 16 0 0 0 0 0 0 0 0 26 28 26 28 26 26 26
1 1 3 5 7 11 17 19 25 10 13 10 15 16 13 10 15 16 0 0 0 0 0 0 0 0 25 26 27 28 25 25 25
2 85 85 85 85 85 85 85 85 85 85 86 85 85 85 12 85 85 85 85 85 85 85 13 85 85 85 85 12 12 85 12 12
1 1 3 5 7 11 17 19 25 10 13 10 15 16 13 10 15 16 0 0 0 0 0 0 0 0 25 27 25 27 25 25 25
2 85 85 85 85 85 85 85 85 85 85 88 85 85 85 12 85 85 85 85 85 85 85 13 85 85 85 85 12 12 85 12 12
2 86 86 86 86 86 86 86 86 86 88 86 88 88 88 26 88 88 88 86 88 88 88 13 88 88 86 86 26 26 86 26 26
3 87 87 87 87 87 87 87 87 87 89 89 90 89 89 89 40 89 89 89 87 89 89 89 41 89 87 87 40 40 40 87 40
1 1 3 5 7 11 17 19 25 10 13 10 15 16 13 10 15 16 0 0 0 0 0 0 0 0 30 30 30 30 30 30 30
2 88 88 88 88 88 88 88 88 88 92 88 92 92 92 58 92 92 92 88 92 92 92 13 92 92 88 88 58 58 88 58 58
3 90 90 90 90 90 90 90 90 90 93 93 90 93 93 93 80 93 93 93 90 93 93 93 41 93 90 90 80 80 80 90 80
2 12 12 12 12 12 12 12 12 12 63 58 63 63 63 12 63 63 63 12 63 63 63 13 63 63 12 12 12 12 12 12 12
3 89 89 89 89 89 89 89 89 89 89 89 93 89 89 89 95 89 89 89 89 89 89 89 41 89 89 89 69 69 69 89 69
3 40 40 40 40 40 40 40 40 40 95 95 80 95 95 95 40 95 95 95 40 95 95 95 41 95 40 40 40 40 40 40 40
3 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41 41
3 40 40 40 40 40 40 40 40 40 69 69 80 69 69 69 40 69 69 69 40 69 69 69 41 69 40 40 40 40 40 40 40
4 91 91 91 91 91 91 91 91 91 94 96 96 96 97 96 96 96 91 96 96 96 98 96 96 96 91 91 99 99 99 91 99
1 1 3 5 7 11 17 19 25 10 0 0 0 0 0 0 0 0 21 18 23 24 21 18 23 24 0 0 0 0 0 0 0
2 101 101 101 101 101 101 101 101 101 101 101 101 101 101 13 101 101 101 101 101 101 101 16 101 101 101 101 16 16 101 16 16
3 102 102 102 102 102 102 102 102 102 102 102 102 102 102 102 41 102 102 102 102 102 102 102 45 102 102 102 45 45 45 102 45
3 45 45 45 45 45 45 45 45 45 45 45 45 45 45 45 41 45 45 45 45 45 45 45 45 45 45 45 45 45 45 45 45
4 103 103 103 103 103 103 103 103 103 103 103 103 103 98 103 103 103 103 103 103 103 104 103 103 103 103 103 104 104 104 103 104
1 0 2 4 6 8 12 18 20 9 13 10 15 16 13 10 15 16 21 18 23 24 21 18 23 24 25 26 27 28 25 25 25
1 0 2 4 6 8 12 18 20 9 13 10 15 16 13 10 15 16 21 18 23 24 21 18 23 24 25 27 25 27 25 25 25
2 106 106 106 106 106 106 106 106 106 107 106 107 107 107 12 107 107 107 106 107 107 107 16 107 107 106 106 20 20 106 20 20
2 107 107 107 107 107 107 107 107 107 107 107 107 107 107 12 107 107 107 107 107 107 107 16 107 107 107 107 31 31 107 31 31
2 106 106 106 106 106 106 106 106 106 107 106 107 107 107 26 107 107 107 106 107 107 107 16 107 107 106 106 20 20 106 20 20
3 108 108 108 108 108 108 108 108 108 109 109 110 109 109 109 40 109 109 109 108 109 109 109 45 109 108 108 52 52 52 108 52
2 107 107 107 107 107 107 107 107 107 107 107 107 107 107 58 107 107 107 107 107 107 107 16 107 107 107 107 31 31 107 31 31
3 110 110 110 110 110 110 110 110 110 112 112 110 112 112 112 80 112 112 112 110 112 112 112 45 112 110 110 82 82 82 110 82
3 109 109 109 109 109 109 109 109 109 109 109 112 109 109 109 69 109 109 109 109 109 109 109 45 109 109 109 72 72 72 109 72
3 52 52 52 52 52 52 52 52 52 72 72 82 72 72 72 40 72 72 72 52 72 72 72 45 72 52 52 52 52 52 52 52
4 111 111 111 111 111 111 111 111 111 113 114 114 114 99 114 114 114 111 114 114 114 104 114 114 114 111 111 115 115 115 111 115
5 54 54 54 54 54 54 54 54 54 74 74 74 84 74 74 74 100 74 74 74 54 74 74 74 105 54 54 116 116 54 116 116
        ]]
    elseif rule == "Hutton32" then
        ruletext = [[
@RULE Hutton32
# Hutton32 -  a modified version of von Neumann's cellular automaton.
# Tim Hutton <tim.hutton@gmail.com>
@TABLE
n_states:32
neighborhood:vonNeumann
symmetries:none
var a={0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31}
var b={0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31}
var c={0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31}
var d={0,8}
var e={0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31}
var f={0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31}
var g={0,1,2,3,4,5,6,7,8,9,10,11,12,13,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31}
var h={0,1,2,3,4,5,6,7,8,9,10,11,12,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31}
var i={0,1,2,3,4,5,6,7,8,9,10,11,12,14,15,16,17,18,19,20,22,23,24,25,26,27,28,29,30,31}
var j={0,1,2,3,4,5,6,7,8,9,10,11,12,13,15,16,17,18,19,20,21,23,24,25,26,27,28,29,30,31}
var k={0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,22,24,25,26,27,28,29,30,31}
var l={0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,18,19,20,21,22,23,25,26,27,28,29,30,31}
var m={5,7}
var n={0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,24,25,26,27,28,29,30,31}
var o={15,23}
var p={0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,25,26,27,28,29,30,31}
var q={0,1,2,3,4,6,7,9,10,11,12,13,14,15,16,21,22,24,25,26,27,28,29,30,31}
var r={0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24,25,26,27,28,29,30,31}
var s={13,27,28,29,31}
var t={9,10,11,12,13,14,15,16,25,26,27,28,29,30,31}
var u={14,27,28,30,31}
var v={0,1,2,3,4,5,6,7,8,9,10,11,12,14,15,16,17,18,19,20,22,23,24,25,26,30}
var w={0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,23,24,25,26,27,28,29,30,31}
var x={5,8,17,18,19,20,23}
var y={16,27,28,30,31}
var z={0,1,2,3,4,5,6,7,8,9,10,11,12,13,15,16,17,18,19,20,21,23,24,25,26,29}
var A={16,24,27,28,30,31}
var B={5,8,17,18,19,20}
var C={0,1,2,3,4,6,7,9,10,11,12,13,14,15,16,21,22,23,25,26,27,28,29,30,31}
var D={15,27,28,29,31}
var E={0,1,2,3,4,6,7,9,10,11,12,13,14,15,16,22,23,24,25,26,27,28,29,30,31}
var F={0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,22,24,25,26,30}
var G={0,1,2,3,4,6,7,9,10,11,12,13,14,15,16,21,23,24,25,26,27,28,29,30,31}
var H={0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,18,19,20,21,22,23,25,26,29}
var I={0,1,2,3}
var J={4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,24,25,26,27,28,29,30,31}
var K={4,8,17,18,19,20}
var L={4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,25,26,27,28,29,30,31}
var M={4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,22,23,24,25,26,27,28,29,30,31}
var N={4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24,25,26,27,28,29,30,31}
var O={17,18,19,20,23}
var P={21,27,28,29,31}
var Q={17,18,19,20,24}
var R={22,27,28,30,31}
var S={17,18,19,20,21}
var T={17,18,19,20,22}
var U={24,27,28,30,31}
var V={23,27,28,29,31}
var W={0,1,2,3,4,5,6,7,8,9,10,11,13,14,15,17,18,19,20,21,22,23,25,26,29}
var X={1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31}
var Y={0,1,2,3,4,5,6,7,8,9,11,12,13,15,16,17,18,19,20,21,23,24,25,26,29}
var Z={0,1,2,3,4,5,6,7,8,10,11,12,14,15,16,17,18,19,20,22,23,24,25,26,30}
var aa={1,2,3,4}
var ab={5,6,7,8}
var ac={5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31}
var ad={0,1,2,3,4,5,6,7,8,10,11,12,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31}
var ae={9,10,11,12,13,14,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31}
var af={0,1,2,3,4,5,6,7,8}
var ag={0,1,2,3,4,5,6,7,8,9,11,12,13,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31}
var ah={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31}
var ai={0,1,2,3,4,5,6,7,8,9,10,12,13,14,16,17,18,19,20,21,22,24,25,26,30}
var aj={5,6,7,8,9,10,11,12,13,14,15,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31}
var ak={9,10,11,12,13,14,15,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31}
var al={0,9,10,11,12,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31}
var am={5,6,7,8,9,10,11,12,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31}
var an={0,1,2,3,4,5,6,7,8,9}
var ao={0,1,2,3,4,5,6,7,8,9,10,11,12,13}
var ap={0,1,2,3,4,5,6,7,8,9,10,12,13,14,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31}
var aq={1,2,3,4,5,6,7,8,9,10,11,12,13,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31}
var ar={5,6,7,8,9,10,11,12,13,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31}
var as={9,10,11,12,13,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31}
var at={25,27}
var au={0,1,2,3,4,5,6,7,8,25,26,27,28,29,30,31}
var av={0,1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20,21,22,24,25,26,27,28,29,30,31}
var aw={0,1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19,20,21,23,24,25,26,27,28,29,30,31}
var ax={0,1,2,3,4,5,6,7,8,10,11,12,14,15,16,17,18,19,20,22,23,24,25,26,27,28,29,30,31}
var ay={0,1,2,3,4,5,6,7,8,9,11,12,13,15,16,17,18,19,20,21,23,24,25,26,27,28,29,30,31}
var az={9,10,11,13,14,15,16,17,18,19,20,21,22,23}
var aA={9,10,11,13,14,15,17,18,19,21,22,23}
var aB={9,10,12,13,14,16,17,18,20,21,22,24}
var aC={0,1,2,3,4,5,6,7,8,9,11,12,13,15,16,17,19,20,21,23,24,25,26,27,28,29,30,31}
var aD={25,30,31}
var aE={10,18}
var aF={0,1,2,3,4,5,6,7,8,10,11,12,14,15,16,18,19,20,22,23,24,25,26,27,28,29,30,31}
var aG={25,29,31}
var aH={9,17}
var aI={25,29,30}
var aJ={11,15,19}
var aK={9,11,12,13,15,16,17,19,20,21,23,24}
var aL={11,19}
var aM={10,11,12,14,15,16,18,19,20,22,23,24}
var aN={0,1,2,3,4,5,6,7,8,10,11,12,13,14,15,16,17,18,19,20,22,23,24,25,26,27,28,29,30,31}
var aO={14,18}
var aP={0,1,2,3,4,5,6,7,8,13,17,25,26,27,28,29,30,31}
var aQ={0,1,2,3,4,5,6,7,8,14,18,25,26,27,28,29,30,31}
var aR={0,1,2,3,4,5,6,7,8,17,25,26,27,28,29,30,31}
var aS={12,20}
var aT={12,16,20}
var aU={9,10,12,13,14,16,17,18,19,20,21,22,24}
var aV={15,19}
var aW={26,28}
var aX={0,1,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,25,26,27,28,29,30,31}
var aY={0,1,2,3,4,5,6,7,8,10,11,12}
var aZ={0,1,2,3,4,5,6,7,8,9,10,12,13,14,16,17,18,19,20,21,22,24,25,26,27,28,29,30,31}
var ba={27,29,30,31}
var bb={13,17}
var bc={29,31}
var bd={29,30}
var be={30,31}
0,a,b,c,13,1
d,e,f,g,21,9
0,a,b,14,h,1
d,e,f,22,i,10
0,a,15,g,h,1
d,e,23,j,i,11
0,16,f,g,h,1
d,24,k,j,i,12
1,e,f,g,h,2
1,a,b,c,13,3
1,a,b,14,h,3
1,a,15,g,h,3
1,16,f,g,h,3
2,e,f,g,h,4
2,a,b,c,13,5
2,a,b,14,h,5
2,a,15,g,h,5
2,16,f,g,h,5
3,e,f,g,h,6
3,a,b,c,13,7
3,a,b,14,h,7
3,a,15,g,h,7
3,16,f,g,h,7
4,e,f,g,h,8
4,a,b,c,13,11
4,a,b,14,i,12
4,a,b,14,21,11
4,a,15,j,i,9
4,a,15,g,21,11
4,a,15,22,i,12
4,16,k,j,i,10
4,16,f,g,21,11
4,16,f,22,i,12
4,16,23,j,i,9
5,l,k,j,i,7
5,a,b,c,13,17
5,e,f,g,21,12
5,a,b,14,i,18
m,a,b,14,21,25
5,e,f,22,i,9
5,a,15,j,i,19
m,a,15,g,21,25
5,a,15,22,i,26
5,e,23,j,i,10
5,16,k,j,i,20
m,16,f,g,21,25
5,16,f,22,i,26
5,16,23,j,i,27
5,24,k,j,i,11
6,e,n,j,i,17
6,a,b,c,13,19
6,e,f,g,21,18
6,a,b,14,i,20
6,a,b,14,21,19
6,e,f,22,i,19
6,a,15,g,21,19
6,a,15,22,i,20
6,e,23,j,i,20
6,16,k,j,i,18
6,16,f,g,21,19
6,16,f,22,i,20
6,16,o,j,i,17
7,l,k,j,i,15
7,a,b,c,13,25
7,e,f,g,21,20
7,a,b,14,i,25
7,e,f,22,i,17
7,a,15,g,i,25
7,e,23,j,i,18
7,16,f,g,i,25
7,24,k,j,i,19
8,a,b,c,13,10
8,a,b,14,i,11
8,a,b,14,21,10
8,a,15,j,i,12
8,a,15,g,21,10
8,a,15,22,i,11
8,16,k,j,i,9
8,16,f,g,21,10
8,16,f,22,i,11
8,16,23,j,i,12
9,p,q,r,s,13
t,a,b,c,21,0
9,p,q,u,v,13
t,a,b,22,w,0
9,a,x,r,s,0
9,a,x,u,v,0
t,a,23,r,w,0
9,y,q,z,v,13
9,A,B,z,v,0
t,24,n,r,w,0
10,C,n,r,s,14
10,C,n,u,v,14
10,C,D,z,v,14
10,B,n,r,s,0
10,B,n,u,v,0
10,B,D,z,v,0
11,p,n,u,E,15
11,p,n,u,B,0
11,p,D,z,E,15
11,p,D,z,B,0
11,y,F,z,E,15
11,y,F,z,B,0
12,p,n,G,s,16
12,p,n,B,s,0
12,p,D,G,v,16
12,p,D,B,v,0
12,y,F,G,v,16
12,y,F,B,v,0
13,H,I,z,v,21
13,H,J,z,v,9
13,p,K,r,s,0
13,p,K,u,v,0
13,H,7,z,v,0
13,p,7,r,s,1
13,p,7,u,v,1
13,y,K,z,v,0
13,y,7,z,v,1
14,I,F,z,v,22
14,L,F,z,v,10
14,K,n,r,s,0
14,K,n,u,v,0
14,K,D,z,v,0
14,7,F,z,v,0
14,7,n,r,s,1
14,7,n,u,v,1
14,7,D,z,v,1
15,H,F,z,I,23
15,H,F,z,M,11
15,H,F,z,7,0
15,p,n,u,K,0
15,p,n,u,7,1
15,p,D,z,K,0
15,p,D,z,7,1
15,y,F,z,K,0
15,y,F,z,7,1
16,H,F,I,v,24
16,H,F,N,v,12
16,p,n,K,s,0
16,H,F,7,v,0
16,p,n,7,s,1
16,p,D,K,v,0
16,p,D,7,v,1
16,y,F,K,v,0
16,y,F,7,v,1
O,a,b,c,13,0
17,e,f,g,P,21
Q,a,b,14,c,0
17,e,f,R,v,21
S,a,15,b,c,0
T,16,a,b,c,0
17,U,f,z,v,21
18,e,f,g,P,22
18,e,f,R,v,22
18,e,V,z,v,22
19,e,f,R,h,23
19,e,V,z,h,23
19,U,F,z,h,23
20,e,f,g,P,24
20,e,V,g,v,24
20,U,F,g,v,24
21,p,0,r,w,17
21,W,X,Y,Z,17
21,a,aa,b,13,13
21,a,aa,14,h,13
21,e,ab,g,9,9
21,a,ac,b,13,0
21,e,ab,10,ad,9
21,a,ac,14,h,0
21,H,ae,z,v,17
21,0,9,10,af,17
21,12,ab,ag,ad,9
21,16,aa,g,h,13
21,16,ac,g,h,0
22,0,n,r,w,18
22,ah,ai,Y,Z,18
22,aa,a,b,13,14
22,aa,a,14,h,14
22,aa,15,g,h,14
22,ab,f,g,9,10
22,aj,a,b,13,0
22,ab,f,10,ad,10
22,aj,a,14,h,0
22,ab,11,ag,ad,10
22,aj,15,g,h,0
22,ak,F,z,v,18
22,9,0,10,af,18
23,W,ai,Y,h,19
23,H,F,z,al,19
23,e,f,10,ab,11
23,p,n,r,0,19
23,a,b,14,aa,15
23,a,b,14,am,0
23,0,11,an,al,19
23,e,11,ag,ab,11
23,0,D,ao,0,19
23,a,15,g,aa,15
23,a,15,g,am,0
23,12,ap,ag,ab,11
23,16,f,g,aa,15
23,16,f,g,am,0
24,p,n,0,w,20
24,W,ai,aq,Z,20
24,a,b,aa,13,16
24,e,f,ab,9,12
24,a,b,ar,13,0
24,H,F,as,v,20
24,e,11,ab,ad,12
24,0,11,9,af,20
24,a,15,aa,h,16
24,a,15,ar,h,0
24,12,ap,ab,ad,12
24,16,f,aa,h,16
24,16,f,ar,h,0
at,au,av,aw,13,26
at,au,av,14,ax,26
at,au,15,ay,ax,26
at,az,au,aw,13,26
at,az,au,14,ax,26
at,aA,aB,aC,13,26
aD,aA,aB,aE,13,29
at,aA,aB,14,aF,26
aG,aA,aB,14,aH,30
aI,aA,aB,14,13,31
aD,aA,aJ,aK,13,29
aG,aA,aL,14,aM,30
at,az,15,au,aN,26
at,aA,15,aK,aF,26
aD,aA,15,aK,aH,29
aD,aA,15,aE,aM,29
at,az,15,aO,aP,26
aI,aA,15,14,aM,31
at,az,19,aQ,13,26
at,az,19,14,aR,26
aD,aS,aB,aK,13,29
aG,aT,aB,14,aM,30
aD,aS,15,aK,aM,29
at,16,au,ay,ax,26
at,16,aU,au,aN,26
at,16,aB,aK,aF,26
aG,16,aB,aK,aH,30
aI,16,aB,aK,13,31
aG,16,aB,aE,aM,30
at,16,aU,aO,aP,26
aG,16,aL,aK,aM,30
at,16,aV,aK,aP,26
aI,16,15,aK,aM,31
at,16,aV,aO,aM,26
at,20,aB,aQ,13,26
at,20,aB,14,aR,26
at,20,15,aK,aP,26
at,20,15,aO,aM,26
at,20,19,aK,13,26
at,20,19,14,aM,26
aW,l,k,j,i,27
26,aX,av,aw,13,28
aW,p,n,10,w,27
26,aX,av,14,ax,28
aW,p,n,aw,9,27
aW,p,11,aw,aN,27
26,0,11,14,aY,27
26,aX,15,ay,ax,28
26,0,15,ao,9,27
26,0,15,10,aY,27
aW,12,av,aw,aN,27
26,12,0,14,aY,27
26,16,aZ,ay,ax,28
ba,l,k,j,i,25
27,p,n,10,w,25
27,p,n,aw,9,25
27,p,11,aw,aN,25
27,0,11,14,aY,25
27,0,15,ao,9,25
27,0,15,10,aY,25
27,aA,aB,14,bb,26
27,aA,aB,18,13,26
27,aA,15,aK,bb,26
27,aA,15,aO,aM,26
27,aA,19,aK,13,26
27,aA,19,14,aM,26
27,12,av,aw,aN,25
27,12,0,14,aY,25
27,16,aB,aK,bb,26
27,16,aB,aO,aM,26
27,16,aV,aK,aM,26
27,20,aB,aK,13,26
27,20,aB,14,aM,26
27,20,15,aK,aM,26
bc,p,k,14,i,30
bd,p,n,14,13,31
bd,p,15,14,i,31
bc,16,k,j,i,30
bd,16,n,j,13,31
bd,16,15,j,i,31
be,l,n,j,13,29
be,l,15,j,i,29
        ]]
    end

    -- add colors
    ruletext = ruletext.. [[
@COLORS
0   48  48  48
1  255   0   0
2  255 125   0
3  255 150  25
4  255 175  50
5  255 200  75
6  255 225 100
7  255 250 125
8  251 255   0
9   89  89 255
10  106 106 255
11  122 122 255
12  139 139 255
13   27 176  27
14   36 200  36
15   73 255  73
16  106 255 106
17  235  36  36
18  255  56  56
19  255  73  73
20  255  89  89
21  185  56 255
22  191  73 255
23  197  89 255
24  203 106 255
25    0 255 128
26  255 128  64
27  255 255 128
28   33 215 215
    ]]

    if rule ~= "JvN29" then
        ruletext = ruletext..[[
29   27 176 176
30   24 156 156
31   21 137 137
        ]]
    end

    return ruletext
end

--------------------------------------------------------------------------------

local function getruletext(rule)
    local ruletext = ""
    local rulesdir = g.getdir("rules")

    -- check for and remove bounded grid postfix
    if rule:find(":") then
        rule = rule:sub(1, rule:find(":") - 1)
    end

    -- attempt to open the rule in the user's rule folder
    local file = io.open(rulesdir..rule..".rule", "r")
    if file == nil then
        -- if not found then check in Golly's Rules folder
        rulesdir = g.getdir("app").."Rules"..pathsep
        file = io.open(rulesdir..rule..".rule", "r")
    end
    if file ~= nil then
        -- read the rule file
        ruletext = file:read("*all")
        file:close()
    end

    return ruletext
end

--------------------------------------------------------------------------------

local function getpattern()
    pattern = nil

    -- get bounding rectangle
    local rect = g.getrect()

    -- get pattern rule
    local rule = g.getrule()

    -- check if pattern is empty
    if #rect == 0 then
        pattern = "#C Exported from Golly by "..myname.."\nx = 0, y = 0, rule = "..rule.."\n!\n"
    else
        local x = rect[1]
        local y = rect[2]
        local wd = rect[3]
        local ht = rect[4]

        -- check if pattern is too big for LifeViewer
        if wd > maxwd or ht > maxht then
            g.note("Pattern is too big for LifeViewer")
            return nil
        end

        local state, last
        local count, cx, cy
        local rowcount = 0
        local charsperrow = 69
        local lastlength = 0
        local rlelength = 0
        local output = {"b", "o"}
        local states = g.numstates()
        local asca = string.byte("A")
        local ascp = string.byte("p")

        -- build the output array if multi-state
        if states > 2 then
            output[1] = "."
            for i = 0, states - 1 do
                if i >= 24 then
                    output[i + 2] = string.char(ascp + (i // 24) - 1)..string.char(asca + i % 24)
                else
                    output[i + 2] = string.char(asca + i)
                end
            end
        end

        -- get cells
        local cells = g.getcells(rect)

        -- check if pattern is 2-state or multi-state
        local inc = 2
        if (#cells & 1) == 1 then
            inc = 3
        end

        -- check if there are too many cells
        if #cells > maxcells * inc then
            g.note("Pattern has too many cells for LifeViewer")
            return nil
        end

        -- create header line
        pattern = "#C Exported from Golly by "..myname.."\nx = "..wd..", y = "..ht..", rule = "..rule.."\n"

        -- create an empty 2d array for the cells
        g.show("Reading cells...")
        cellarray = {}
        for i = 1, ht do
            cellarray[i] = {}
            for j = 1, wd do
                cellarray[i][j] = 0
            end
        end

        -- read each cell (x, y) for 2-state, (x, y, state) for multi-state
        state = 1
        n = 1
        while (n < #cells) do
            cx = cells[n]
            cy = cells[n + 1]
            if (inc == 3) then
                state = cells[n + 2]
            end
            cellarray[cy - y + 1][cx - x + 1] = state
            n = n + inc
        end

        -- create RLE from the 2d array
        g.show("Building RLE...")
        local rle = {}
        local r = 1
        i = 1
        local cellrow = cellarray[i]
        while i <= ht do
            j = 1
            last = cellrow[j]
            count = 1
            j = j + 1
            while j <= wd + 1 do
                if j > wd then
                    state = -1
                else
                    state = cellrow[j]
                end
                if state ~= last then
                    if not (state == -1 and last == 0) and rowcount > 0 then
                        if (rowcount > 1) then
                            rle[r] = rowcount
                            r = r + 1
                            rlelength = rlelength + tostring(rowcount):len()
                        end
                        rle[r] = "$"
                        r = r + 1
                        rlelength = rlelength + 1
                        if rlelength - lastlength >= charsperrow then
                            rle[r] = "\n"
                            r = r + 1
                            rlelength = rlelength + 1
                            lastlength = rlelength
                        end
                        rowcount = 0
                    end
                    if last > 0 then
                        if count > 1 then
                            rle[r] = count
                            r = r + 1
                            rlelength = rlelength + tostring(count):len()
                        end
                        rle[r] = output[last + 1]
                        r = r + 1
                        rlelength = rlelength + output[last + 1]:len()
                    else
                        if j <= wd then
                            if count > 1 then
                                rle[r] = count
                                r = r + 1
                                rlelength = rlelength + tostring(count):len()
                            end
                            rle[r] = output[last + 1]
                            r = r + 1
                            rlelength = rlelength + output[last + 1]:len()
                        end
                    end
                    if rlelength - lastlength >= charsperrow then
                        rle[r] = "\n"
                        r = r + 1
                        rlelength = rlelength + 1
                        lastlength = rlelength
                    end
                    count = 1
                    last = state
                else
                    count = count + 1
                end
                j = j + 1
            end
            rowcount = rowcount + 1
            i = i + 1
            cellrow = cellarray[i]
        end
        rle[r] = "!\n"
        pattern = pattern..table.concat(rle)
        g.show("")
    end

    -- add pattern comments
    pattern = pattern.."\n"..g.getinfo()

    -- check for RuleLoader algo
    local algo = g.getalgo()
    if algo == "RuleLoader" then
        pattern = pattern.."\n"..getruletext(rule)
    elseif algo == "JvN" then
        pattern = pattern.."\n"..getJvNruletext(rule)
    end

    -- return the RLE
    return pattern
end

--------------------------------------------------------------------------------

local function launchBrowser(uri)
    -- execute the file to open the browser
    local opersys = g.os()
    if opersys == "Windows" then
        os.execute("start \"\" \""..uri.."\"")
    elseif opersys == "Linux" then
        os.execute("xdg-open \""..uri.."\"")
    elseif opersys == "Mac" then
        os.execute("open \""..uri.."\"")
    end
end

--------------------------------------------------------------------------------

local function createDirectory(path)
    local opersys = g.os()
    if opersys == "Windows" then
        os.execute("mkdir \""..path.."\"")
    elseif opersys == "Linux" then
        os.execute("mkdir -p \""..path.."\"")
    elseif opersys == "Mac" then
        os.execute("mkdir -p \""..path.."\"")
    end
end

--------------------------------------------------------------------------------

local function launchLifeViewer()
    -- check LifeViewer exists in Golly's Scripts/Lua/gplus folder
    local lifeviewerdir = g.getdir("data")..lifeviewerfolder..pathsep
    local lifeviewerpath = lifeviewerdir..lifeviewerfilename
    local file, msg = io.open(lifeviewerpath, "r")
    if file == nil then
        -- prompt to download LifeViewer (Cancel will abort script)
        g.note("LifeViewer is not installed!\n\n"..msg.."\n\nClick OK to go to download page or Cancel to stop.\n\n"..lifeviewerdownload)

        -- attempt to create the LifeViewer folder
        createDirectory(lifeviewerdir)

        -- open the default browser at the download page
        launchBrowser(lifeviewerdownload.."?dir="..lifeviewerpath)
    else
        file:close()

        -- path for the launch file in the Golly temp directory so it will be deleted when Golly exits
        local filename = g.getdir("temp")..launchfilename

        -- construct the pattern RLE
        local pattern = getpattern()
        if pattern ~= nil then
            -- create the launch file contents
            local content = [[
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF8">
        <meta name="LifeViewer" content="viewer textarea 150 fullscreen">
]]
            content = content.."\t\t<script src=\"file:"..pathsep..pathsep..pathsep..lifeviewerpath.."\"></script>\n"..
[[
        <title>LifeViewer - Golly</title>
    </head>
    <body>
        <div class="viewer">
]]
            content = content.."\t\t<canvas width=\""..viewerwidth.."\" height=\""..viewerheight.."\"></canvas>\n"..
[[
            <br>
            <br>
            <textarea rows=5 cols=99>
]]
            content = content..pattern
            content = content..
[[
            </textarea>
            <br>
        </div>
    </body>
</html>
]]
            -- create the launch file
            file, msg = io.open(filename, "w")
            if file == nil then
                g.note("Could not create launch file!\n\n"..msg)
            else
                file:write(content)
                file:close()

                launchBrowser(filename)
            end
        end
    end
end

--------------------------------------------------------------------------------

local _, err = xpcall(launchLifeViewer, gp.trace)
if err then g.continue(err) end

-- this code is always executed, even after escape/error;
g.check(false)
