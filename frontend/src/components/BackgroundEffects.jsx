import React from 'react';
import { motion } from 'framer-motion';

const BackgroundEffects = () => {
  return (
    <div className="fixed inset-0 -z-10 overflow-hidden bg-background">
      {/* Mesh Gradient Overlay */}
      <div className="absolute inset-0 opacity-40 mesh-gradient animate-hue-shift" />
      
      {/* Dot Grid */}
      <div className="absolute inset-0 dot-grid opacity-20" />

      {/* Floating Orbs */}
      <motion.div
        animate={{
          x: [0, 100, -50],
          y: [0, -100, 50],
          scale: [1, 1.2, 1],
        }}
        transition={{
          duration: 20,
          repeat: Infinity,
          ease: "linear"
        }}
        className="absolute -top-20 -left-20 w-96 h-96 bg-primary/10 rounded-full blur-[100px]"
      />
      
      <motion.div
        animate={{
          x: [0, -150, 100],
          y: [0, 50, -100],
          scale: [1, 1.1, 1],
        }}
        transition={{
          duration: 25,
          repeat: Infinity,
          ease: "linear"
        }}
        className="absolute top-1/2 -right-20 w-[500px] h-[500px] bg-success/10 rounded-full blur-[120px]"
      />

      <motion.div
        animate={{
          x: [0, 80, -20],
          y: [0, 120, -50],
        }}
        transition={{
          duration: 18,
          repeat: Infinity,
          ease: "linear"
        }}
        className="absolute -bottom-40 left-1/3 w-[600px] h-[600px] bg-warning/5 rounded-full blur-[150px]"
      />
    </div>
  );
};

export default BackgroundEffects;
