%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%% GWSG2ML %%%%%%%%%%%%%%%  script by Eduardo Becker Groth
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


tic
logical=1;
if logical == 1;
    script = ' script';
else
    script = ' noGUI';
end

pathl=strcat('abaqus cae ',script,'="','C:\Users\Groth\Desktop\models_ml\tira_zero','\','tira_zero1.py','"');
dos(pathl);

%%
cd('C:\Users\Groth\Desktop\models_ml\tira_zero\results')
u0= importdata('u0.txt');  % nome dos arquivos .txt   
figure 
hold on
plot(u0.data(:,1),u0.data(:,2))
plot(u0.data(:,1),u0.data(:,3))
toc