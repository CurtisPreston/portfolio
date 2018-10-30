import processing.core.*; 
import processing.data.*; 
import processing.event.*; 
import processing.opengl.*; 

import java.util.*; 

import java.util.HashMap; 
import java.util.ArrayList; 
import java.io.File; 
import java.io.BufferedReader; 
import java.io.PrintWriter; 
import java.io.InputStream; 
import java.io.OutputStream; 
import java.io.IOException; 

public class node_garden extends PApplet {


ArrayList<node> nodes = new ArrayList<node>();
int max_dis=255;
boolean bo=true;


public void setup(){


//fullScreen();

//noLoop();
for(int x=0;x<35;x++){
nodes.add(new node((int)random(width),(int)random(height)));
}

println(nodes.size());
println(nodes);
}



public void draw(){
  background(255);
  

  
  for(int i=0;i<nodes.size();i++){
    node chk=nodes.get(i);
    for(int e=i+1;e<nodes.size();e++){
      node to=nodes.get(e);
      float dis=distance(chk.x,chk.y,to.x,to.y);
      if(dis<max_dis){
        stroke(0,0,0, -dis+255);
        strokeWeight((-dis+255)/25);
        line(chk.x,chk.y,to.x,to.y);
        
      }
    }
    fill(255);
    stroke(0);
    strokeWeight(1);
    ellipse(chk.x,chk.y,50,50);
    chk.update();
  }
  //fill(0);
  //text(frameRate,100,100);
  //text(nodes.size(),150,100);
  
}





  
  





public float distance(float x,float y,float x2,float y2){
  float dis = sqrt(sq(x-x2)+sq(y-y2));
  
  return dis;
}



public void keyPressed(){
bo=false;
}


public void mousePressed(){


nodes.add(new node(mouseX,mouseY));
}



class node{
  
  float spd=random(4)+0.1f;
  float x,y;
  float dx=0;
  float dy=0;
node(float x1,float y1){
x=x1;
y=y1;
dx= generateRandom(2);
dy=generateRandom(2);



}

public void update(){

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
    
    float random = (rand.nextFloat()*max)+0.1f;

    if(rand.nextBoolean()){
      random=-random;
    }
    
    

    return random;
}

}
  public void settings() { 
size(800,800); }
  static public void main(String[] passedArgs) {
    String[] appletArgs = new String[] { "node_garden" };
    if (passedArgs != null) {
      PApplet.main(concat(appletArgs, passedArgs));
    } else {
      PApplet.main(appletArgs);
    }
  }
}
