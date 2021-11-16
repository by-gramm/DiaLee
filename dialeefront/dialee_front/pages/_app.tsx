import  '../styles/global.css'
import type { AppProps } from 'next/app'
import {ThemeProvider} from 'styled-components'
import Footer from "../components/organisms/footer"
import axios from 'axios'
import { RecoilRoot,useRecoilValue} from 'recoil';
import {BASED_URL} from '../lib/constants'
import {basicTheme, retroTheme,springTheme,summerTheme,fallTheme,winterTheme} from '../styles/theme';
import Head from 'next/head'




axios.defaults.baseURL = BASED_URL;
axios.defaults.withCredentials = true;

function MyApp({ Component, pageProps }: AppProps) {
 

  return (<>
  <RecoilRoot>
  <Head><link rel="preconnect" href="https://fonts.googleapis.com"/>
    <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="true"/>
    <link href="https://fonts.googleapis.com/css2?family=Nanum+Brush+Script&family=Nanum+Myeongjo&display=swap" rel="stylesheet"/></Head>
  <ThemeProvider theme={springTheme}>
 
  <Component {...pageProps} />

  </ThemeProvider>
  </RecoilRoot>
 </> )

}
export default MyApp
