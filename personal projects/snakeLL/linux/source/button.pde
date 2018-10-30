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
  
  
  void ds(){
  rect(x,y,xsize,ysize);
  text(name,x,y);  
}
  
  
  
  void setpressed(){
    pressed=(mouseX>x && mouseX<x+xsize && mouseY>y &&mouseY<y+ysize);
  }
  
  boolean getpressed(){
    return pressed;
  }

}
