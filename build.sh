py -3 -m venv .venv                    
.venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
reflex init
reflex export --frontend-only
Remove-Item -Recurse -Force public
mkdir public
Expand-Archive -Path frontend.zip -DestinationPath public
Remove-Item -Force frontend.zip
deactivate

#Deploy
reflex deploy --no-interactive -k ceramica -r eze --env URL="https://gcjyhrlcftbkeaiqlzlm.supabase.co" --env KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImdjanlocmxjZnRia2VhaXFsemxtIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTU3MjQ3NzAsImV4cCI6MjAzMTMwMDc3MH0.MFsm9DJ9XnVnsTUK-N2SsCBf8wnhW03mGp5d2Z2Jf9Q" --env SERVICE_ROLE="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImdjanlocmxjZnRia2VhaXFsemxtIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcxNTcyNDc3MCwiZXhwIjoyMDMxMzAwNzcwfQ.HC-tuFM2oMqJt2jjbuRHJ3fdLbXIMnn4OtBGBPcufwA" --env WPP_SID="ACbf995101c557f1a4f756fceb563c23c8" --env WPP_TOKEN="da18f909d1abb2bed57cb4e86fab40fa" #Produccion
reflex deploy --no-interactive -k ceramica -r eze --env URL="https://gcjyhrlcftbkeaiqlzlm.supabase.co" --env KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImdjanlocmxjZnRia2VhaXFsemxtIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTU3MjQ3NzAsImV4cCI6MjAzMTMwMDc3MH0.MFsm9DJ9XnVnsTUK-N2SsCBf8wnhW03mGp5d2Z2Jf9Q" --env SERVICE_ROLE="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImdjanlocmxjZnRia2VhaXFsemxtIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcxNTcyNDc3MCwiZXhwIjoyMDMxMzAwNzcwfQ.HC-tuFM2oMqJt2jjbuRHJ3fdLbXIMnn4OtBGBPcufwA" --env WPP_SID="ACa88ee24037331b208c3ba842117e2e52" --env WPP_TOKEN="3c9c6b05ffd6da8f3969d52938262485" #Respaldo

