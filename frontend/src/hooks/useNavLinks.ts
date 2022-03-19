interface INavLink {
  text: string;
  link: string;
  icon: string;
}

const navLinks: INavLink[] = [
  { text: "Home", link: "/", icon: "dashboard" },
  { text: "Create", link: "wallet", icon: "create" },
];

export function useNavLinks() {
  return navLinks;
}
