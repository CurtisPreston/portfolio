bodypart snake = new bodypart();
int rows=20;
int sq_size;
int direction=0;
boolean playing=true;
Fruit fruit=new Fruit();
button pl = new button(100,100,100,25,"play again");
button exit = new button(400,100,100,25,"exit");

void setup(){
size(512,512);
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



void draw(){
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



void menu(){


pl.ds();


exit.ds();


if(exit.getpressed()){
exit();
}
if(pl.getpressed()){
reset();

}
}

void reset(){
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


void mousePressed(){
pl.setpressed();
exit.setpressed();
}

void keyPressed(){
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
