import { useEffect } from 'react';
import styled from 'styled-components';
import DisabledDiv from '../../atoms/disabledDiv';
import FlexContainer from '../../atoms/flexcontainer';
import Image from '../../atoms/image';
import loadingState from '../../../atom/loadingState';
import { useRecoilValue } from 'recoil';
const StyledLoadingImg=styled.div`
    animation:imgRotationAnim 1s infinite;
    z-index:10000;

    @keyframes imgRotationAnim{
        from
        {
            transform:rotate(0deg);
        }
        to
        {   
            transform:rotate(360deg);
        }
    }
`
const MainLoading =()=>{
    const isLoading=useRecoilValue(loadingState);

    return(<>
        {isLoading===true&&
        <DisabledDiv height="100vh">
            <FlexContainer direction="column" align="center" alignItems="center">
                로딩중
                <StyledLoadingImg>
                    <Image src="/imoticon/SunFlower.png" width="100px" height="100px"></Image>
                </StyledLoadingImg>
            </FlexContainer>
        </DisabledDiv>}
        </>
    )
}

export default MainLoading ;