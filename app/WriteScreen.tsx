import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

export default function WriteScreen() {
  return (
    <View style={styles.container}>
      <Text style={styles.text}>Write Screen</Text>
      <Text>This screen will be used to write new posts.</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  text: {
    fontSize: 20,
    fontWeight: 'bold',
  },
});
