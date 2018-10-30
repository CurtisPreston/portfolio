class Fruit{
  int x;
  int y;
  Fruit(){
  x=(int)random(20);
  y=(int)random(20);
  }
  
  
  void randomize(){
  x=(int)random(20);
  y=(int)random(20);
  }
  
  
  void ds(){
  fill(color(255,0,0));
  rect(x*sq_size,y*sq_size,sq_size,sq_size);
  }
}
