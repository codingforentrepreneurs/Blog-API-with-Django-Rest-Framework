
'''
curl -X POST -d "username=cfe&password=learncode" http://127.0.0.1:8000/api/auth/token/

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImNmZSIsInVzZXJfaWQiOjEsImVtYWlsIjoiIiwiZXhwIjoxNDYxOTY1ODI5fQ.OTX7CZFZqxhaUnU9Da13Ebh9FY_bHMeCF1ypr9hXjWw

curl -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImNmZSIsInVzZXJfaWQiOjEsImVtYWlsIjoiIiwiZXhwIjoxNDYxOTY1ODI5fQ.OTX7CZFZqxhaUnU9Da13Ebh9FY_bHMeCF1ypr9hXjWw
" http://127.0.0.1:8000/api/comments/


curl -X POST -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImNmZSIsInVzZXJfaWQiOjEsImVtYWlsIjoiIiwiZXhwIjoxNDYxOTY2MTc4fQ._i5wEqJ_OO8wNiVVNAWNPGjGaO7OzChY0UzONgw06D0" -H "Content-Type: application/json" -d '{"content":"some reply to another try"}' 'http://127.0.0.1:8000/api/comments/create/?slug=new-title&type=post&parent_id=13'



curl http://127.0.0.1:8000/api/comments/



curl -X POST -d "username=anotheruser123&password=anotheruser123" http://127.0.0.1:8000/api/auth/token/


eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFub3RoZXJ1c2VyMTIzIiwidXNlcl9pZCI6NywiZW1haWwiOiJhbm90aGVydXNlcjEyM0BnbWFpbC5jb20iLCJleHAiOjE0NjE5NjY0ODF9.KZ991-PGIm63BKikMbDSdFStStJ6uu6WtsraAmbo7BQ

curl -X POST -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFub3RoZXJ1c2VyMTIzIiwidXNlcl9pZCI6NywiZW1haWwiOiJhbm90aGVydXNlcjEyM0BnbWFpbC5jb20iLCJleHAiOjE0NjE5NjY0ODF9.KZ991-PGIm63BKikMbDSdFStStJ6uu6WtsraAmbo7BQ" -H "Content-Type: application/json" -d '{"content":"my new reply to another try"}' 'http://127.0.0.1:8000/api/comments/create/?slug=new-title&type=post&parent_id=13'



'''
