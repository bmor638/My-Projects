package part2;

import java.util.*;
import java.io.*;
import java.math.BigInteger;

public class Part2 {
	
    public static void main(String[] args) {
    	
    	System.out.println(solovayStrassen(new BigInteger("15373"), 55));
    	System.out.println("Numerical confidence that the number is prime: " + (1-stillCompositeProbability(55)));
    	   	
    	// get user input for file paths for n, e, d, and ascii text
//    	Scanner scanner = new Scanner(System.in);
//    	
//    	System.out.println("Would you like to generate a key (G), encrypt text (E), or decrypt text (D)? ");
//    	String option = scanner.nextLine();
//    	
//    	if (option.equals("G")) {
//    		
//    		// find prime values for 'p' and 'q' using Solovay-Strassen
//    		BigInteger p = findPrime();
//    		BigInteger q = findPrime();
//    		
//    		// calculate 'n' by multiplying 'p' and 'q'
//    		BigInteger n = p.multiply(q);
//    		
//    		// save 'n' to file 'newN.txt'
//    		try {
//				FileWriter nWriter = new FileWriter("newN.txt");
//				nWriter.write(n.toString());
//				nWriter.close();
//			} catch (IOException e) {
//				e.printStackTrace();
//			}
//    		
//    		// find a random value for 'e' that is relatively prime to phi of 'n'
//    		BigInteger phiN = p.subtract(BigInteger.ONE).multiply(q.subtract(BigInteger.ONE));
//    		Random random = new Random();
//    		BigInteger e;
//    		do {
//    			e = new BigInteger(phiN.bitLength(), random);
//    		} while (!e.gcd(phiN).equals(BigInteger.ONE));
//    		
//    		// save 'e' to file 'newE.txt'
//    		try {
//				FileWriter eWriter = new FileWriter("newE.txt");
//				eWriter.write(e.toString());
//				eWriter.close();
//			} catch (IOException e1) {
//				e1.printStackTrace();
//			}
//    		
//    		// find 'd' (the inverse of 'e' mod 'phiN')
//    		BigInteger d = e.modInverse(phiN);
//    		
//    		// save 'd' to file 'newD.txt'
//    		try {
//				FileWriter dWriter = new FileWriter("newD.txt");
//				dWriter.write(d.toString());
//				dWriter.close();
//			} catch (IOException e2) {
//				e2.printStackTrace();
//			}
//    		
//    		System.out.println("\nAll done! Your keys have been written to files \"newN.txt\", \"newE.txt\", and \"newD.txt\" respectively.");
//    		
//    	} else if (option.equals("E") || option.equals("D")) {
//    	
//    		// get user input for file path to 'n'
//	    	System.out.println("Enter file path for n: ");
//	    	String nFilePath = scanner.nextLine();
//	    	
//	    	// get user input for file path to 'e'
//	    	System.out.println("\nEnter file path for e: ");
//	    	String eFilePath = scanner.nextLine();
//	    	
//	    	// deal with 'd' only if decrypting
//	    	BigInteger d = null;
//	    	if (option.equals("D")) {
//	    		
//	    		// get user input for file path to 'd'
//		    	System.out.println("\nEnter file path for d: ");
//		    	String dFilePath = scanner.nextLine();
//		    	
//		    	// read in 'd' from 'dFile'
//		    	File dFile = new File(dFilePath);
//		    	Scanner dScanner = null;
//				try {
//					dScanner = new Scanner(dFile);
//				} catch (FileNotFoundException e1) {
//					e1.printStackTrace();
//				}
//				
//		    	while (dScanner.hasNextBigInteger()) {
//		    		d = dScanner.nextBigInteger();
//		    	}
//		    	
//		    	dScanner.close();
//	    	}
//	    	
//	    	// get user input for file path to ascii text
//	    	System.out.println("\nEnter file path for content: ");
//	    	String file = scanner.nextLine();
//    	
//	    	// read in 'n' from 'nFile'
//	    	File nFile = new File(nFilePath);
//	    	Scanner nScanner = null;
//			try {
//				nScanner = new Scanner(nFile);
//			} catch (FileNotFoundException e) {
//				e.printStackTrace();
//			}
//	    	BigInteger n = null;
//	    	while (nScanner.hasNextBigInteger()) {
//	    		n = nScanner.nextBigInteger();
//	    	}
//	    	
//	    	nScanner.close();
//    	
//   
//	    	// read in 'e' from 'eFile'
//	    	File eFile = new File(eFilePath);
//	    	Scanner eScanner = null;
//			try {
//				eScanner = new Scanner(eFile);
//			} catch (FileNotFoundException e) {
//				e.printStackTrace();
//			}
//	    	BigInteger e = null;
//	    	while (eScanner.hasNextBigInteger()) {
//	    		e = eScanner.nextBigInteger();
//	    	}
//	    	
//	    	eScanner.close();
//	    	
//	    	// perform encryption operations
//	    	if (option.equals("E")) {
//	    		
//		    	// call 'readToBytes' function to get a byte array of the ascii text
//		        byte[] bytes = null;
//		        try {
//		        
//					bytes = readToBytes(file);
//				
//		        } catch (FileNotFoundException e1) {
//					e1.printStackTrace();
//				}
//		        
//		        // break 'bytes' into 214-byte blocks
//		        ArrayList<BigInteger> blocks = breakIntoBlocks(bytes);
//		    		
//		        // perform encryption
//		        ArrayList<BigInteger> ciphertextBlocks = encryptBlocks(blocks, e, n);
//		        
//		        // print encrypted ciphertext blocks
//		        System.out.println("Encrypted ciphertext:\n");
//		        for (BigInteger block : ciphertextBlocks) {
//		        	System.out.print(block.toString() + "\n");
//		        }
//		        
//	    	} else if (option.equals("D")) {
//	    		
//	    		// add blocks from 'file' to array list
//	    		ArrayList<BigInteger> blocks = new ArrayList<BigInteger>();
//	    		
//	    		// read in blocks from 'file'
//		    	File fileObj = new File(file);
//		    	Scanner fileScanner = null;
//				try {
//					fileScanner = new Scanner(fileObj);
//				} catch (FileNotFoundException e1) {
//					e1.printStackTrace();
//				}
//				
//				// add block to list
//		    	while (fileScanner.hasNextBigInteger()) {
//		    		blocks.add(fileScanner.nextBigInteger());
//		    	}
//		    	
//		    	fileScanner.close();
//
//		        // perform decryption on 'ciphertextBlocks'
//		        String plaintext = decryptBlocks(blocks, d, n);
//		        
//		        // print decrypted ciphertext
//		        System.out.println("\nDecrypted ciphertext:\n" + plaintext);
//		    	}
//    		}
//        
//        scanner.close();
    }


    
   
    
    public static BigInteger findPrime() {
    	
    	// compute the number of values needed to verify that n is a prime
    	//		with probability of at most 10^-14 of still being composite after Solovay-Strassen tests
    	int k = calculateK(Math.pow(10, -14));
    	
    	BigInteger n = null;
    	boolean found = false;
    	Random random = new Random();
    	int tries = 0;
    	
    	while (!found) {
    		
    		// could have generated a 1022-bit number and put a 1 in the first and last bit...
    		// choose a random 1024-bit number
    		n = new BigInteger(1024, random);
    		
    		// check if 'n' is even
    		if (n.mod(BigInteger.TWO).equals(BigInteger.ZERO)) {
    			n = n.add(BigInteger.ONE);
    		}
    			
    		// perform 'k' Solovay-Strassen tests on 'n'
			boolean result = solovayStrassen(n, k);
			
			// increment 'tries' if 'n' turned out composite
			if (!result) {
				tries++;
				
			// exit while loop if 'n' is probably prime
			} else {
				found = true;
			}
    	}
    	
    	// print numerical information
    	System.out.println("\n****NUMERICAL INFORMATION****");
    	System.out.println("Number of (odd) random numbers tried before finding prime: " + tries);
    	System.out.println("Number of values used to verify that the number is prime: " + k);
    	System.out.println("Numerical confidence that the number is prime: " + (1-stillCompositeProbability(k)));
    	
    	return n;
    }
    
    
    
    
    
    // read in the ascii plaintext/ciphertext from 'filename' into a byte array
    public static byte[] readToBytes(String filename) throws FileNotFoundException {
        
    	File file = new File(filename);
        Scanner scanner = new Scanner(file);
        List<Byte> bytes = new ArrayList<Byte>();

        // read the contents of the file into 'bytes'
        while (scanner.hasNextInt()) {
        	
            // convert each ascii character to a byte and add to 'bytes'
            bytes.add((byte) scanner.nextInt());
        }

        scanner.close();

        // convert 'bytes' to a byte array
        byte[] byteArray = new byte[bytes.size()];
        for (int i = 0; i < bytes.size(); i++) {
            byteArray[i] = bytes.get(i);
        }

        return byteArray;
    }
    
    
    
    
    
    public static ArrayList<BigInteger> breakIntoBlocks(byte[] bytes) {
    	
    	ArrayList<BigInteger> blocks = new ArrayList<BigInteger>();
    	BigInteger currentBlock = BigInteger.ZERO;
    	int blockSize = 0;
    	int byteIndex = 0;
    	
    	while (byteIndex < bytes.length) {
    		
    		// add the next byte from 'bytes' to 'currentBlock'
    		currentBlock = currentBlock.add(BigInteger.valueOf(bytes[byteIndex]));
    		
    		// shift 'currentBlock' to the left by a byte (8 bits)
    		currentBlock = currentBlock.shiftLeft(8);
    		
    		// increment 'blockSize' and 'byteIndex'
    		blockSize++;
    		byteIndex++;
    		
    		// add 'currentBlock' to 'blocks' if 'currentBlock' is 214-bytes
    		if (blockSize == 214) {
    			
    			// remove extra left shift from 'currentBlock'
    			currentBlock = currentBlock.shiftRight(8);
    			
    			blocks.add(currentBlock);
    			
    			// reset 'blockSize' and 'currentBlock'
    			blockSize = 0;
    			currentBlock = BigInteger.ZERO;
    		}
    	}
    	
    	// remove extra left shift from 'currentBlock'
    	currentBlock = currentBlock.shiftRight(8);
    	
    	// add the last 'currentBlock' to 'blocks'
    	blocks.add(currentBlock);
    	
    	return blocks;
    }


    
    
    
    public static ArrayList<BigInteger> encryptBlocks(ArrayList<BigInteger> blocks, BigInteger e, BigInteger n) {

        ArrayList<BigInteger> ciphertextBlocks = new ArrayList<BigInteger>();
        
        // form 214-byte blocks
        for (int i = 0; i < blocks.size(); i++) {

            // encrypt each block individually
            BigInteger ciphertext = modularExponentiation(blocks.get(i), e, n);

            // convert 'ciphertext' to String and append to 'ciphertextString'
            ciphertextBlocks.add(ciphertext);
        }

        return ciphertextBlocks;
    }


    
    
    
    public static String decryptBlocks(ArrayList<BigInteger> blocks, BigInteger d, BigInteger n) {
        
        String plaintextString = new String();

        // form 214-byte blocks
        for (int i = 0; i < blocks.size(); i += 214) {

            // decrypt each block individually
            BigInteger plaintext = modularExponentiation(blocks.get(i), d, n);

            // make 'plaintext' into a byte array
            byte[] plaintextBytes = plaintext.toByteArray();
            
            // concatenate 'plaintextString' with each char in 'plaintextBytes'
            for (byte b : plaintextBytes) {
            	plaintextString += (char) b;
            }
        }

        return plaintextString;
    }
    
    
    
    
    
    // perform the Solovay-Strassen test 'k' times
    //		returns 'true' if probably prime, 'false' if composite
    private static boolean solovayStrassen(BigInteger n, int k) {
    	
    	Random random = new Random();
    	
    	// complete SS procedure 'k' times
    	for (int i = 0; i < k; i++) {
	    	
    		// pick a random value for 'a' with 1 < a < n-1
	    	BigInteger a;
	    	do {
	    		a = new BigInteger(1024, random);
	    	} while (a.compareTo(BigInteger.ONE) <= 0 || a.compareTo(n.subtract(BigInteger.ONE)) >= 0);
	    	
	    	// return 'false' if gcd(a,n) != 1
	    	if (!(gcd(a,n).equals(BigInteger.ONE))) {
	    		System.out.println("breaks at gcd");
	    		return false;
	    	}
	    	
	    	// evaluate Euler's criterion
	    	BigInteger eulerCriterion = a.modPow(n.shiftRight(1), n);
	    	
	    	// return 'false' if 'eulerCriterion' != +-1
	    	if (!(eulerCriterion.equals(BigInteger.ONE)) && !(eulerCriterion.equals(n.subtract(BigInteger.ONE)))) {
	    		System.out.println("breaks at euler criterion");
	    		return false;
	    	}
	    	
	    	// if 'eulerCriterion' is n-1, then reset it to -1
	    	if (eulerCriterion.equals(n.subtract(BigInteger.ONE))) {
	    		eulerCriterion = BigInteger.ONE.negate();
	    	}
	    	
	    	// evaluate the Jacobi symbol
	    	BigInteger jacobi = jacobi(a,n);
	    	
	    	// return 'false' if the Jacobi symbol does not equal the Euler criterion
	    	if (!(jacobi.equals(eulerCriterion))) {
	    		System.out.println("breaks at jacobi");
	    		return false;
	    	}
	    }
    	
    	// return 'true' if 'n' passed 'k' tests
    	return true;
    }
    
    
    
    
    
    // private helper method to compute the greatest common divisor
    private static BigInteger gcd(BigInteger n, BigInteger m) {
    	if (m.equals(BigInteger.ZERO)) {
    		return n;
    	} else {
    		return gcd(m, n.mod(m));
    	}
    }
    
    
    
    
    // private helper method to evaluate b^e (mod m)
    private static BigInteger modularExponentiation(BigInteger b, BigInteger e, BigInteger m) {

        BigInteger result = BigInteger.ONE;

        while (e.compareTo(BigInteger.ZERO) > 0) {

            if (e.mod(BigInteger.valueOf(2)).equals(BigInteger.ONE)) {
                result = (result.multiply(b)).mod(m);
            }

            b = (b.multiply(b)).mod(m);
            e = e.divide(BigInteger.valueOf(2));
        }
        
        return result;
    }
    
    
    
    

    private static BigInteger jacobi(BigInteger a, BigInteger n) {

        // initially reduce 'a' mod 'n'
        a = a.mod(n);

        // initialize 'result' to 1
        BigInteger result = BigInteger.ONE;

        while (!(a.equals(BigInteger.ZERO))) {
            
        	// check if 'a' is even
            while ((a.mod(BigInteger.valueOf(2))).equals(BigInteger.ZERO)) {
                
            	// pull out 2s from 'a'
                a = a.divide(BigInteger.valueOf(2));

                // apply rule 3
                BigInteger r = n.mod(BigInteger.valueOf(8));
                if (r.equals(BigInteger.valueOf(3)) || r.equals(BigInteger.valueOf(5))) {
                    result = result.negate();
                }
            }

            // flip 'a' and 'n'
            BigInteger temp = a;
            a = n;
            n = temp;

            // apply rule 5
            if ((a.mod(BigInteger.valueOf(4))).equals(BigInteger.valueOf(3)) && (n.mod(BigInteger.valueOf(4))).equals(BigInteger.valueOf(3))) {
                result = result.negate();
            }

            // reduce 'a' mod 'n'
            a = a.mod(n);
        }

        if (n.equals(BigInteger.ONE)) {
            return result;
        } else {
        	
            // return 0 if 'a' and 'n' are not relatively prime
            return BigInteger.ZERO;
        }
    }
    
    
    
    
    
    // determine the number of values (k) needed to verify that a number is probably prime
    private static int calculateK(double upperLimit) {
    	
    	int k = 1;
    	double compositeProb = stillCompositeProbability(k);
    	
    	// increment 'k' until the probability given by 'confidence' is greater than 'upperLimit'
    	while (compositeProb > upperLimit) {
    		k++;
    		compositeProb = stillCompositeProbability(k);
    	}
    	
    	// return 'k'
    	return k;
    }
    
    
    
    
    
    // compute the probability (as a percentage) that a 1024-bit number is composite 
    //		given that it passes Solovay-Strassen 'k' times
    private static double stillCompositeProbability(int k) {
    	double numerator = (1024*Math.log(2))-2;
    	double denominator = (1024*Math.log(2))-2+Math.pow(2, k+1);
    	
    	return (numerator/denominator);
    }
    
    
    
    
    
    // use the extended Euclidean algorithm to compute the inverse of a number 'm' (mod 'n')
    private static BigInteger extendedEuclidean(BigInteger m, BigInteger n) {
        BigInteger xNegOne = BigInteger.ONE;
        BigInteger yNegOne = BigInteger.ZERO;
        BigInteger xZero = BigInteger.ZERO;
        BigInteger yZero = BigInteger.ONE;

        while (!n.equals(BigInteger.ZERO)) {
            BigInteger[] divAndRem = m.divideAndRemainder(n); // get quotient and remainder
            BigInteger q = divAndRem[0];
            BigInteger r = divAndRem[1];

            BigInteger x = xNegOne.subtract(q.multiply(xZero));
            BigInteger y = yNegOne.subtract(q.multiply(yZero));

            m = n;
            n = r;

            xNegOne = xZero;
            yNegOne = yZero;
            xZero = x;
            yZero = y;
        }

        // ensure the result is non-negative
        BigInteger result = xNegOne;
        if (result.compareTo(BigInteger.ZERO) == -1) {
        	result = result.add(n);
        }
        return result;
    }
}



// C:/Users/Beckett Morris/OneDrive - University of Denver/Documents/Second Year/Spring/COMP 3705/project3/src/part2/n.txt
