class bodypart{
  int x=0;
  int y=0;
  bodypart next;
  void ds(){
    fill(color(255,255,255));
    rect(x*sq_size,y*sq_size,sq_size,sq_size);
    if(next!=null){
    next.ds();
    }
  }
  
  boolean colide(int x1,int y1){
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
  boolean removelast(){
  
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
