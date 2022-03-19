interface INavLink {
  text: string;
  link: string;
  icon: string;
}

const navLinks: INavLink[] = [
  { text: "Home", link: "/", icon: "dashboard" },
  { text: "Create", link: "create", icon: "create" },
];

export function useNavLinks() {
  return navLinks;
}
