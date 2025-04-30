// app/components/App.js

import React, { useEffect, useState } from "react";
import { View, Text, Button } from "react-native";

export default function App() {
  const [users, setUsers] = useState([]);

  // GET 요청
  useEffect(() => {
    fetch("http://43.201.26.92:5001/users")
      .then((res) => res.json())
      .then((data) => setUsers(data))
      .catch((err) => console.log(err));
  }, []);

  // POST 요청 예시
  const addUser = () => {
    fetch("http://43.201.26.92:5001/users", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ name: "seungpyo", email: "rush94434@gmail.com" }),
    })
      .then((res) => res.json())
      .then((data) => console.log(data));
  };

  return (
    <View style={{ padding: 40 }}>
      <Text style={{ fontSize: 18, marginBottom: 10 }}>📋 유저 목록</Text>
      {users.map((u, i) => (
        <Text key={i}>• {u.name} ({u.email})</Text>
      ))}
      <Button title="사용자 추가" onPress={addUser} />
    </View>
  );
}
