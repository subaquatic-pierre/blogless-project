interface INotificationState {
  isOpen: boolean;
  message: string;
  color: AlertColor;
}

interface INotificationMethods {
  setError: (message: string) => void;
  setSuccess: (message: string) => void;
  setInfo: (message: string) => void;
  setWarning: (message: string) => void;
  clearNotification: () => void;
}
