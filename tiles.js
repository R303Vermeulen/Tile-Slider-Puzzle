let tiles = [];


function setup() 
{
   createCanvas(500, 500);
   background(150,150,150);
   for(let i = 0; i<9; i++)
      tiles[i] = i

   //noLoop();
}

function draw()
{
   background(150,150,150);
   for(let i=0; i<9; i++)
   {
      let x = 100 + 100 * (i%3)
      let y = 100 + 100 * ((i - i%3) / 3)
      
      if(tiles[i] == 0)
      {
         fill(0);
         rect(x, y, 100, 100);
      }
      else
      {
         fill(255);
         rect(x, y, 100, 100);
         fill(0);
         textSize(30);
         text(tiles[i], x+40, y+60)
      }
      
   }

}


function keyTyped()
{
   let spot = -1
   for(let i=0; i<9; i++)
   {
      if(tiles[i] == 0)
      {
         spot = i
      }
   }
   if(key == 'w')
   {
      if(spot > 2)
      {
         tiles[spot] = tiles[spot-3]
         tiles[spot-3] = 0
      }
   }
   if(key == 's')
   {
      if(spot < 6)
      {
         tiles[spot] = tiles[spot+3]
         tiles[spot+3] = 0
      }
   }
   if(key == 'd')
   {
      if(spot % 3 < 2)
      {
         tiles[spot] = tiles[spot+1]
         tiles[spot+1] = 0
      }
   }
   if(key == 'a')
   {
      if(spot % 3 > 0)
      {
         tiles[spot] = tiles[spot-1]
         tiles[spot-1] = 0
      }
   }



}
