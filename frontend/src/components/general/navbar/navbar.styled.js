import styled from "styled-components";

const NavWrapper = styled.nav`
  position: sticky;
  font-size: 1.6rem;
  font-weight: 500;
  display: flex;
  height: 81px;
  padding-inline: ${({ mobile, tablet }) =>
    mobile ? "40px" : tablet ? "78.9px" : "120px"};
  width: 100%;
  background: #091540;
`;

const NavItemsWrapper = styled.ul`
  position: relative;
  display: flex;
  width: 100%;
  justify-content: space-between;
  align-items: center;
`;
const LogoWrapper = styled.div`
  width: ${({ mobile, tablet }) =>
    mobile ? "48.9%" : tablet ? "73.46%" : "164.63px"};
  height: ${({ mobile, tablet }) =>
    mobile ? "48.9%" : tablet ? "73.46%" : "49px"};
  & > img{
    width:100%;
    height:100%
    object-fit:cover;
  }
`;

const Items = styled.li`
  display: flex;
  gap: 40px;
  align-items: center;
  &.nav--link--items {
    display: ${({ tablet }) => tablet && "none"};
  }
  & > a {
    transition: 200ms all ease-in-out;
    display: flex;
  }
  & > a.active {
    color: #c04a1c;
  }
`;

const MobileNavWrapper = styled.div`
  position: absolute;
  right: 0;
  left: 0;
  background: #091540;
  display: flex;
  flex-direction: column;
  gap: 10px;
  top: 100%;
  font-weight: 500;
  font-size: 10px;
  line-height: 28px;
  overflow-x: hidden;
  transition: 300ms 0.2s all ease-in-out;
  height: 0px;
  padding-inline: ${({ mobile, tablet }) =>
    mobile ? "40px" : tablet ? "78.9px" : "120px"};
  &.open {
    height: 180px;
    max-height: fit-content;
  }
  & > a.active {
    transition: 200ms all ease-in-out;
    color: #c04a1c;
  }
`;
export { NavItemsWrapper, NavWrapper, LogoWrapper, Items, MobileNavWrapper };
