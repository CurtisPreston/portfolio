
ArrayList<node> nodes = new ArrayList<node>();
int max_dis=255;
boolean bo=true;


void setup(){


//fullScreen();
size(800,800);
//noLoop();
for(int x=0;x<35;x++){
nodes.add(new node((int)random(width),(int)random(height)));
}

println(nodes.size());
println(nodes);
}



void draw(){
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





  
  





float distance(float x,float y,float x2,float y2){
  float dis = sqrt(sq(x-x2)+sq(y-y2));
  
  return dis;
}



void keyPressed(){
bo=false;
}


void mousePressed(){


nodes.add(new node(mouseX,mouseY));
}