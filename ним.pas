var n1,n2,k,number:integer;
f:boolean;
begin
f:=true;
n1:=0; 
n2:=0;
while n1<=0 do 
  begin
  write('введите кол-во камней в первой куче: ');
  readln(n1);
  end;
while n2<=0 do 
  begin
  write('введите кол-во камней во второй куче: ');
  readln(n2);
  end;
  writeln;
while (n1>0)or(n2>0) do
  begin
  writeln('ХОД КОМПЬЮТЕРА');
  if(n1=n2)then
    begin
    n1:=n1-1;
    writeln('компьютер взял из первой кучи 1 камень');
    end
  else
    begin
    if n1>n2 then 
      begin  
      k:=n1-n2;
      n1:=n1-k;
      writeln('компьютер взял из первой кучи ',k,' камней');
      end
    else 
      begin
      k:=n2-n1;
      n2:=n2-k;
      writeln('компьютер взял из второй кучи ',k,' камней');
      end;
    end;
  writeln('в куче 1 осталось ',n1,' камней');
  writeln('в куче 2 осталось ',n2,' камней');
  writeln;
  if (n1=0)and(n2=0) then
    begin
    writeln('В этот раз выйграл компьютер!');
    f:=false; 
    end;
  if f=true then 
    begin
    writeln('ХОД ПОЛЬЗОВАТЕЛЯ');
    number:=0;
    while(number<>1)and(number<>2) do
      begin
      write('введите номер кучи: ');
      readln(number);
      end;
    if number=1 then
      begin
      k:=0;
        while(k>n1)or(k<=0)do
          begin
          write('введите кол-во камней: ');
          readln(k);
          end;
      n1:=n1-k;
      end
     else 
      begin 
     k:=0; 
     while(k>n2)or(k<=0)do
      begin
      write('введите кол-во камней: '); 
      readln(k);
      end;
      n2:=n2-k;
      end;
    writeln('в первой куче осталось ',n1,' камней');
    writeln('во второй куче осталось ',n2,' камней');
    writeln;
      if (n1=0)and(n2=0) then 
        writeln('Поздравляем, Вы победили!');
    end;
  end;
end.
