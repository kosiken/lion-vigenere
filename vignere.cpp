#include <iostream>
#include <cstring>
#include <string>
#include <random>
#include <cmath>

using namespace std;
bool panic(char *values, char *keys);

void printIt(const char *words, const char *keys, bool decoded = true);

void decode(const char *values, const char *keys);

void encode(const char *values, char const *keys);

char *replace(const char *word, char r, char wit);
string  getRandomKey( const char *values);



int main(int argc, char const *argv[])
{
	
	//cout  << *(argv+1)<< endl; 
	
	string help = "usage: ./vigenere [-h] [-k key] [-e] [-f FILE] text\n"

"Vigenere Cipher Decoding Utiliy Author: kosiken<allisonkosy@gmail.com>\n"

"positional arguments:\ntext        The text to decrypt or encrypt"

"\noptional arguments:\n  -h, --help  show this help message and exit\n"
  "-k key      The key to use to decrypt or encrypt the text\n"
  "-e          Change mode to encrypt the text\n"
  "-f FILE     The path to file you want to write\n"

"example: $python ./vignere abcd -k ztuw --file dest.txt\n";

		
	
	string err = "Error too few arguments : Usage vigenere [-h] [-k key] [-e] [-f FILE] text ";
	
	if (argc == 1) {
		//cout << "lo";
		cout << err << endl; 
		}
		
	else if(argc == 2 && string(argv[1]) != string( "-h")) {
		
		cout << err << *(argv+1)<< endl; 
		
		
		}
		
		else if (argc == 2 && string(argv[1]) == string( "-h")) {
		
		cout << help << endl; 
		
		
		}
		
		else if (argc == 3) {
			
		if(string(argv[2]) == string("-e") ){
			const char * text = argv[1];
			string  ke = getRandomKey(text);
			
			encode(text,ke.c_str());
			
			} 
		}
		else if (argc == 4) {

             decode(argv[1], argv[3]); 
             //<< endl;

        }

  

      
    return 0;

}

bool panic(char *values, char *keys){
    return (strlen(replace(values, ' ', '\0'))!= strlen(keys));
}

char *replace(const char *word, char r, char wit)
{
    char *rep = new char;
   // char *e = "lion";
    int length = strlen(word);
    int t = 0;

    for (int i = 0; i < length; i++)
    {

        char w = *(word + i);

        if (w == r)
        {
            if (wit != '\0')
            {
                *(rep + t) = wit;
                t++;
            }
        }
        else
        {
             *(rep + t) = w;
                t++;


        }
    }

    return rep;
}


void printIt(const char *words, const char *keys, bool decoded ) {
    string val = decoded ? "Decoded: " : "Encoded: ";
    string keys_str(keys), words_str(words);

    val = val + words_str;


    val = val + ("\nKey: " + keys_str);

    cout << val << endl;
    


};

void decode(const char *values, const char *keys){
    string alphabet = "abcdefghijklmnopqrstuvwxyz";
    string decoded = "";
    int index = 0;
    string val(values);
    string ke(keys);


    

    for(char v: val) {

        if(v == ' ') {
            decoded = decoded + ' ';
            continue;

        }

		int ine= alphabet.find(v), inr = alphabet.find(ke[index]);

        int pos = ( ine - inr);
        pos = 0 > pos ? 26 + pos : pos % 26;
         
         pos = abs(pos);
         
         decoded = decoded + alphabet[pos];
         index++;

    }
    printIt(decoded.c_str(), keys);
};

void encode(const char *values,const char *keys){
    string alphabet = "abcdefghijklmnopqrstuvwxyz";
    string encoded = "";
    int index = 0;
    string val(values);
    string ke(keys);


    

    for(char v: val) {

        if(v == ' ') {
            encoded = encoded + ' ';
            continue;

        }


        int pos = ((alphabet.find(v)
        + alphabet.find(ke[index]))
         % alphabet.length());

         encoded = encoded + alphabet[pos];
         index++;

    }
     printIt(encoded.c_str(), ke.c_str(), false);
};

string getRandomKey(const char *values){
    
    string key = "";
    
    //= "";
    string alphabet = "abcdefghijklmnopqrstuvwxyz";

   int length =  strlen(replace(values, ' ', '\0'));
   for(int i = 0; i<length; i++) {


       int randomn = random()%26;
      
     key= key + alphabet[randomn];
      
   }


   return key;
};
