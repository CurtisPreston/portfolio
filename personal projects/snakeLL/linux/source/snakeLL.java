import processing.core.*; 
import processing.data.*; 
import processing.event.*; 
import processing.opengl.*; 

import java.util.HashMap; 
import java.util.ArrayList; 
import java.io.File; 
import java.io.BufferedReader; 
import java.io.PrintWriter; 
import java.io.InputStream; 
import java.io.OutputStream; 
import java.io.IOException; 

public class snakeLL extends PApplet {

bodypart snake = new bodypart();
int rows=20;
int sq_size;
int direction=0;
boolean playing=true;
Fruit fruit=new Fruit();
button pl = new button(100,100,100,25,"play again");
button exit = new button(400,100,100,25,"exit");

public void setup(){

sq_size=width/rows;
frameRate(5);
snake.x=rows/2;
snake.y=rows;
for(int x=1;x<3;x++){
bodypart n = new bodypart();
n.x=rows/2;
n.y=rows-x;
n.next=snake;
snake=n;
}

}



public void draw(){
  background(0);
  for(int y=0;y<rows;y++){
    line(y*sq_size,0,y*sq_size,width);
  }
  for(int y=0;y<rows;y++){
    line(0,y*sq_size,height,y*sq_size);
  }
  
  snake.ds();
  fruit.ds();
  bodypart n=new bodypart();
  if(playing){
  switch(direction){
  case 0:
    n.x=snake.x;
    n.y=snake.y-1;
    break;
  case 1:
    n.x=snake.x-1;
    n.y=snake.y;
    break;
  case 2:
    n.x=snake.x;
    n.y=snake.y+1;
    break;
  case 3:
    n.x=snake.x+1;
    n.y=snake.y;
    break;
  }
  
  
  n.next=snake;
  
  snake=n;
  
  
  if(snake.x<0||snake.x>rows||snake.y<0||snake.y>rows){
  playing=false;
  }
  
  if(snake.next!=null){
  if(snake.next.colide(snake.x,snake.y)){
  playing=false;
  }
  }
  
  if(snake.x==fruit.x && snake.y==fruit.y){
    fruit.randomize();
  }else{
    snake.removelast();
  }
  }else{
  menu();
  }
  
}



public void menu(){


pl.ds();


exit.ds();


if(exit.getpressed()){
exit();
}
if(pl.getpressed()){
reset();

}
}

public void reset(){
  snake = new bodypart();
snake.x=rows/2;
snake.y=rows;
for(int x=1;x<3;x++){
bodypart n = new bodypart();
n.x=rows/2;
n.y=rows-x;
n.next=snake;
snake=n;
}
fruit.randomize();
playing=true;
}


public void mousePressed(){
pl.setpressed();
exit.setpressed();
}

public void keyPressed(){
if(key=='w' && direction!=2){
direction=0;
}
if(key=='a'&& direction!=3){
direction=1;
}
if(key=='s'&& direction!=0){
direction=2;
}
if(key=='d'&& direction!=1){
direction=3;
}
}
class bodypart{
  int x=0;
  int y=0;
  bodypart next;
  public void ds(){
    fill(color(255,255,255));
    rect(x*sq_size,y*sq_size,sq_size,sq_size);
    if(next!=null){
    next.ds();
    }
  }
  
  public boolean colide(int x1,int y1){
  if(x1==x && y1==y){
    return true;
  }else{
    if(next!=null){
    return next.colide(x1,y1);
  }else{
    return false;
  }

}
  }  
  public boolean removelast(){
  
    if(next==null){
      return true;
    }else{
      if(next.removelast()){
        next=null;
    return false;
      }
    }
    return false;
    
  }
}
class button{
int x,y,xsize,ysize;
String name=""; 
boolean pressed=false;
  button(int x,int y,int xsize,int ysize,String name){
  this.x =x;
  this.y=y;
  this.xsize=xsize;
  this.ysize=ysize;
  this.name=name;
  }
  
  
  public void ds(){
  rect(x,y,xsize,ysize);
  text(name,x,y);  
}
  
  
  
  public void setpressed(){
    pressed=(mouseX>x && mouseX<x+xsize && mouseY>y &&mouseY<y+ysize);
  }
  
  public boolean getpressed(){
    return pressed;
  }

}
class Fruit{
  int x;
  int y;
  Fruit(){
  x=(int)random(20);
  y=(int)random(20);
  }
  
  
  public void randomize(){
  x=(int)random(20);
  y=(int)random(20);
  }
  
  
  public void ds(){
  fill(color(255,0,0));
  rect(x*sq_size,y*sq_size,sq_size,sq_size);
  }
}
  public void settings() { 
size(512,512); }
  static public void main(String[] passedArgs) {
    String[] appletArgs = new String[] { "snakeLL" };
    if (passedArgs != null) {
      PApplet.main(concat(appletArgs, passedArgs));
    } else {
      PApplet.main(appletArgs);
    }
  }
}
