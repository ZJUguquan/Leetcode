# 1306 Sequence Median 

class Scanner {
   InputStream in;
   char c;
   Scanner(InputStream in) {
      this.in = in;
      nextChar();
   }
   void asserT(boolean e) {
      if (!e) {
         throw new Error();
      }
   }
   void nextChar() {
      try {
         c = (char)in.read();
      } catch (IOException e) {
         throw new Error(e);
      }
   }

   long nextLong() {
      while (true) {
         if ('0' <= c && c <= '9') {
            break;
         }
         asserT(c != -1);
         nextChar();
      }
      long value = c - '0';
      nextChar();
      while ('0' <= c && c <= '9') {
         value *= 10;
         value += c - '0';
         nextChar();
      }
      return value;
   }

   int nextInt() {
      long longValue = nextLong();
      int intValue = (int)longValue;
      asserT(intValue == longValue);
      return intValue;
   }
}


// 
// System.out.print( (a+b)/2 );
//             if ( (a+b) % 2==0){
//             } else {
//                 System.out.println(".5");
//             }