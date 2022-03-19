import React from "react";
import { AlertColor } from "@mui/material/Alert";
import { initialNotificationState } from "context/initialState";

export const NotificationContext = React.createContext<
  [INotificationState, INotificationMethods | null]
>([initialNotificationState, {} as INotificationMethods]);

const NotificationContextProvider: React.FC = ({ children }) => {
  const [notificationState, setNotificationState] =
    React.useState<INotificationState>(initialNotificationState);

  const parseState = (
    oldState: INotificationState,
    message: string,
    color: AlertColor
  ) => {
    return {
      ...oldState,
      isOpen: true,
      message: message,
      color: color,
    };
  };

  const clearNotification = () => {
    setNotificationState((oldState) => ({
      ...oldState,
      isOpen: false,
    }));
  };

  const setError = (message: string) => {
    setNotificationState((oldState) => parseState(oldState, message, "error"));
  };

  const setSuccess = (message: string) => {
    setNotificationState((oldState) =>
      parseState(oldState, message, "success")
    );
  };

  const setInfo = (message: string) => {
    setNotificationState((oldState) =>
      parseState(oldState, message, "warning")
    );
  };

  const setWarning = (message: string) => {
    setNotificationState((oldState) =>
      parseState(oldState, message, "warning")
    );
  };

  const notificationMethods: INotificationMethods = {
    setError,
    setSuccess,
    setInfo,
    setWarning,
    clearNotification,
  };

  return (
    <NotificationContext.Provider
      value={[notificationState, notificationMethods]}
    >
      {children}
    </NotificationContext.Provider>
  );
};

export default NotificationContextProvider;
