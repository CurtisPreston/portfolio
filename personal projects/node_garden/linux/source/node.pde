import java.util.*;


class node{
  
  float spd=random(4)+0.1;
  float x,y;
  float dx=0;
  float dy=0;
node(float x1,float y1){
x=x1;
y=y1;
dx= generateRandom(2);
dy=generateRandom(2);



}

void update(){

if( x<0 || x>width)
  dx=-dx;
  if( y<0 || y>height)
    dy=-dy;

x+=dx;
y+=dy;  
}
  


public float generateRandom(int max) {
    Random rand = new Random();
    //int range = end - start + 1;

    //int random = rand.nextInt(end) -start;
    //while(excludeRows.contains(random)) {
    //    random = rand.nextInt(end) -start;
    //}
    
    float random = (rand.nextFloat()*max)+0.1;

    if(rand.nextBoolean()){
      random=-random;
    }
    
    

    return random;
}

}
