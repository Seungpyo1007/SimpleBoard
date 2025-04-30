// app/components/UserList.tsx

import React from 'react';
import { View, Text, Button } from 'react-native';

const UserList = ({ users, addUser }) => {
  if (!users) {
    // users가 undefined일 경우 빈 배열로 처리
    users = [];
  }

  return (
    <View style={{ padding: 20 }}>
      <Text style={{ fontSize: 20, marginBottom: 10 }}>User List</Text>
      {users.length === 0 ? (
        <Text>No users found.</Text>
      ) : (
        users.map((user, index) => (
          <Text key={index}>
            {user.name} ({user.email})
          </Text>
        ))
      )}
      <Button title="Add User" onPress={addUser} />
    </View>
  );
};

export default UserList;
