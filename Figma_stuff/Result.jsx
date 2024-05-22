import { Box, Button, Container, FormLabel, HStack, Heading, Input, VStack } from '@chakra-ui/react'
import React, { useState } from 'react'
import { Link } from 'react-router-dom';
import {useDispatch} from "react-redux"
import { login } from '../../REDUX/actions/user';

const Login = () => {

  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const dispatch = useDispatch()

  const submitHandler = (e)=>{

    e.preventDefault();
    dispatch(login(email, password))
  }

  return (
    <Container h = {'95vh'}>
        <VStack h={'full'} justifyContent={"center"} spacing={'16'}>
            <Heading children={"WELCOME BACK TO COURSEWORK"} color={"antiquewhite"}/>

            <form onSubmit={submitHandler} style={{width: '100%'}}>
              <div style={{width: 139, height: 36, paddingLeft: 16, paddingRight: 16, background: '#1976D2', borderRadius: 4, justifyContent: 'flex-start', alignItems: 'center', gap: 16, display: 'inline-flex'}}>
                <div style={{width: 107, alignSelf: 'stretch', paddingTop: 11, paddingBottom: 11, justifyContent: 'flex-start', alignItems: 'center', gap: 8, display: 'flex'}}>
                  <div style={{textAlign: 'center', color: 'white', fontSize: 14, fontFamily: 'Roboto', fontWeight: '500', textTransform: 'uppercase', lineHeight: 36, letterSpacing: 1.25, wordWrap: 'break-word'}}>CONTAINED</div>
                  <div style={{width: 12, textAlign: 'center', color: 'white', fontSize: 16, fontFamily: 'Material Icons', fontWeight: '400', lineHeight: 16, wordWrap: 'break-word'}}>cancel</div>
                </div>
              </div>
              <Box my={"2"}>
              <FormLabel htmlFor = "email" children="Email" color={"antiquewhite"}/>
              <Input required id="email" 
                     value={email} 
                     onChange={e => setEmail(e.target.value)} 
                     placeholder='abc@gmail.com'
                     type={'email'}
                     focusBorderColor="purple.500"
                     color={"antiquewhite"}
                      />

              </Box>

              <Box my={"6"}>
              <FormLabel htmlFor = "password" children="Password" color={"antiquewhite"}/>
              <Input required id="password" 
                     value={password} 
                     onChange={e => setPassword(e.target.value)} 
                     placeholder='Enter Your Password'
                     type={'password'}
                     focusBorderColor="purple.500"
                     color={"antiquewhite"}
                      />
              </Box>

              <HStack spacing={"10"}justifyContent={"flex-start"}>
                
              <Button my="4" colorScheme={'purple'} type='submit' variant={"ghost"}>
                Login 
              </Button>
           
              <Box my={"2"}>
                
                New USER? <Link to={"/Register"}>
                    <Button colorScheme='purple'variant={"link"}>SIGN UP</Button> {" "}
                    here
                     </Link>
              </Box>
              

              </HStack>

              
              <Box height={"6"}>
                <Link to="/ForgotPassword">
                  <Button fontSize={'sm'} variant="link" >
                    I FORGOT MY PASSWORD
                  </Button>
                </Link>


              </Box>
            

          </form>
        </VStack>
    </Container>

  );
}
export default Login