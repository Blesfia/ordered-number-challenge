--ghc 7.10
--
import Data.Char
import Data.List

-- Define function to determinates if two numbers needs to be improved
needsImprove :: String -> Bool
-- Base case with less than 2 digits
needsImprove [] = False
needsImprove [x1] = False
-- General case
needsImprove (x1:x2:xs) = x1 < x2

-- Decrease an string number based on first 2 digits
decreaseDigit :: String -> String
-- Base case with less than 2 digits
decreaseDigit [] = []
decreaseDigit [x1] = [x1]
-- Case when first digit is 0, then return 9 & (n2-1)
decreaseDigit ('0':x2:xs) = "9" ++ [chr(ord x2 - 1)]
-- General case, then return (n1 - 1) & n2
decreaseDigit (x1:x2:xs) = chr (ord x1 - 1) : [x2]

-- Build a new number with old and new digits
buildNumber (x0:xs) (r0:rs) = if r0 == '9' then '9':r0:rs else x0:r0:rs

-- Main process to order a number
processNumber :: String -> String
-- Base case when number is less than 10
processNumber [] = []
processNumber [x1] = [x1]
-- General case
processNumber (x1:x2:xs) =
  if needsImprove [x1, x2]
    -- Case when number is not ordered
    then processNumber(decreaseDigit (x1 : [x2]) ++ xs)
    -- Case when number is ordered
    else buildNumber (x1:x2:xs) (processNumber (x2:xs))
  
-- Start the process to improve a number
start :: String -> String
start str = show(read(reverse $ processNumber $ reverse str)::Int)::String

-- Process input file and returns a list with processed numbers
processInputFile [x1] = [start x1]
processInputFile (x1:xs) =
  (start x1) : (processInputFile xs)

-- Main function
main = do
  input <- readFile "entrada.txt"
  let linesOfFile = lines input
  let result = processInputFile $ tail linesOfFile
  writeFile "salida.txt" (intercalate "\n" result)
